import re
import threading

import riffyn_nexus_sdk_v1 as api
import requests

from lib import riffyn, utils
from plugins.riffyn.config import PluginConfig
from src.commands import command

cfg = PluginConfig()


class Watcher(threading.Thread):
    def __init__(self, logger, cache, queue, done):
        super(Watcher, self).__init__()

        self.logger = logger
        self.cache = cache
        self.queue = queue
        self.done = done
        self.cache_key = cfg.CACHE_KEY
        self.poll_interval = cfg.POLL_INTERVAL

        client = riffyn.Client.default(cfg.API_KEY)
        self.activity_api = api.ProcessActivityApi(client)
        self.experiment_api = api.ExperimentApi(client)
        self.run_api = api.RunApi(client)

        self.partials = {}

    def run(self):
        while not self.done.is_set():
            self.logger.info("runs.poll.started")

            try:
                runs = self.__fetch_run_statuses()
                for experiment_id, runs in runs.items():
                    for run in runs["started"]:
                        self.logger.info(
                            "run.started",
                            experiment_id=experiment_id,
                            run_id=run.id,
                            run_name=run.name,
                        )

                        complete, plate = self.__aggregate(run)
                        if len(complete) > 0:
                            if plate:
                                commands = self.__build_commands(
                                    experiment_id, complete, plate
                                )
                            else:
                                commands = self.__build_commands(
                                    experiment_id, complete
                                )

                            for cmd in commands:
                                self.queue.put(cmd)

                        self.cache.hset(self.cache_key, run.id, "")

                    for run in runs["stopped"]:
                        self.logger.info(
                            "run.stopped",
                            experiment_id=experiment_id,
                            run_id=run.id,
                            run_name=run.name,
                        )

                        partial = self.__is_partial(run)
                        if partial:
                            key, rows, cols, idx = partial
                            if key in self.partials:
                                self.partials[key][idx] = None

                        self.cache.hdel(self.cache_key, run.id)

                self.logger.info("runs.poll.finished")

            except api.rest.ApiException as err:
                self.logger.error(
                    "runs.poll.failed", status=err.status, error=err.reason
                )

            except Exception as err:
                self.logger.error("runs.poll.failed", error=err)

            self.done.wait(self.poll_interval)

    def __fetch_run_statuses(self):
        experiments = self.__fetch_experiments()
        active_runs = self.cache.hgetall(self.cache_key)

        runs = {}
        for experiment in experiments:
            status = {"started": [], "stopped": []}
            for run in self.__fetch_runs(experiment.id):
                if run.status == "running" and run.id not in active_runs:
                    status["started"].append(run)

                elif (
                    run.status == "stopped" or run.status == "new"
                ) and run.id in active_runs:
                    status["stopped"].append(run)

            runs[experiment.id] = status

        return runs

    def __fetch_experiments(self):
        experiments = self.experiment_api.list_experiments()
        return experiments.data

    def __fetch_runs(self, experiment_id):
        groups = self.run_api.list_run_groups(experiment_id)
        runs = list(
            map(
                lambda group: self.run_api.list_runs(experiment_id, group.id).data,
                groups.data,
            )
        )
        return utils.flatten(runs)

    def __aggregate(self, run):
        partial = self.__is_partial(run)
        if not partial:
            return [run], None

        key, rows, cols, idx = partial
        if key not in self.partials:
            # Pre-fill an array equal to the number of expected partials
            self.partials[key] = [None] * (rows * cols)
        self.partials[key][idx] = run

        # Check that all partial runs in the aggregated set have been populated
        if all(partial is not None for partial in self.partials[key]):
            return self.partials[key], (rows, cols)

        return [], None

    def __is_partial(self, run):
        partial = re.search(r"(.*) \[([1-9])+x([1-9])+\] ([1-9])+$", run.name)
        if not partial:
            return False

        name, rows, cols, idx = partial.group(1, 2, 3, 4)
        key = f"{self.cache_key}/{run.activity_id}/{name}"
        return (key, int(rows), int(cols), int(idx) - 1)

    def __build_commands(self, experiment_id, runs, plate=None):
        activity = self.activity_api.get_activity(experiment_id, runs[0].activity_id)
        data = self.__get_experiment_data_raw(experiment_id, activity.id, runs)
        commands = self.__init_commands(experiment_id, activity, runs, plate)

        for api_version, (cmd, resources) in commands.items():
            properties = {}
            for input in activity.inputs:
                if input.id in resources:
                    for property in input.properties:
                        header = f"{activity.id} | input | {input.id} | {property.id} | value"
                        properties[utils.str_to_camelcase(property.name)] = header

            for idx, run in enumerate(runs):
                spec = {}
                for property, header in properties.items():
                    datatable = data["datatables"][run.id]["datatable"][0]
                    value = datatable[header]

                    if value is not None:
                        spec[property] = value

                if isinstance(cmd.spec, list):
                    cmd.spec[idx] = spec
                else:
                    cmd.spec = spec

        return [cmd for (cmd, resources) in commands.values()]

    def __get_experiment_data_raw(self, experiment_id, activity_id, runs):
        resp = requests.get(
            f"https://api.app.riffyn.com/v1/experiment/{experiment_id}/step/{activity_id}/data/raw",
            headers={"api-key": cfg.API_KEY},
            params={
                "rgid": list(map(lambda run: run.group_id, runs)),
                "rid": list(map(lambda run: run.id, runs)),
                "rnum": list(map(lambda run: run.num, runs)),
            },
        )
        resp.raise_for_status()
        return resp.json()

    def __init_commands(self, experiment_id, activity, runs, plate=None):
        # Create a mapping of API version -> (command, resource IDs)
        commands = {}
        protocol = activity.name.replace(" ", "")

        for input in runs[0].inputs:
            try:
                api_version = input.resource_name
                if api_version not in commands:
                    cmd = command.Command(api_version, protocol)

                    if plate:
                        cmd.plate(*plate)
                        # Pre-fill the spec with an array equal to the number of runs
                        cmd.spec = [None] * len(runs)
                        cmd.metadata(
                            "riffyn",
                            list(
                                map(
                                    lambda run: {
                                        "experimentId": experiment_id,
                                        "activityId": activity.id,
                                        "runId": run.id,
                                    },
                                    runs,
                                )
                            ),
                        )

                    else:
                        cmd.metadata(
                            "riffyn",
                            {
                                "experimentId": experiment_id,
                                "activityId": activity.id,
                                "runId": runs[0].id,
                            },
                        )

                    commands[api_version] = (cmd, [])

                commands[api_version][1].append(input.resource_def_id)

            except command.InvalidAPIVersion:
                continue

        return commands
