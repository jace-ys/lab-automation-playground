import threading

import requests
import swagger_client as riffyn

from lib import utils
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

        riffyn.Configuration().api_key["api-key"] = cfg.API_KEY
        self.activity_api = riffyn.ProcessActivityApi()
        self.experiment_api = riffyn.ExperimentApi()
        self.run_api = riffyn.RunApi()

    def run(self):
        while not self.done.is_set():
            self.logger.info("runs.poll.started")

            try:
                runs = self.__fetch_run_statuses()
                for experiment_id, runs in runs.items():
                    for run in runs["started"]:
                        try:
                            cmd = self.__build_command(experiment_id, run)
                            self.queue.put(cmd)

                            self.cache.hset(self.cache_key, run.id, "")
                            self.logger.info("run.started", run_id=run.id)

                        except command.InvalidAPIVersion:
                            pass  # No-op

                    for run in runs["stopped"]:
                        self.logger.info("run.stopped", run_id=run.id)
                        self.cache.hdel(self.cache_key, run.id)

                self.logger.info("runs.poll.finished")

            except riffyn.rest.ApiException as err:
                self.logger.error(
                    "runs.poll.failed", status=err.status, error=err.reason
                )
                raise

            except Exception as err:
                self.logger.error("runs.poll.failed", error=err)
                raise

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

                elif run.status == "stopped" and run.id in active_runs:
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

    def __build_command(self, experiment_id, run):
        activity = self.activity_api.get_activity(experiment_id, run.activity_id)

        data = self.__get_experiment_data_raw(experiment_id, activity.id, run)
        datatable = data["datatables"][run.id]["datatable"][0]

        if run.inputs:
            # NOTE: Assume the first input's resource is the target
            api_version = run.inputs[0].resource_name
        elif run.outputs:
            # NOTE: Assume the first output's resource is the target
            api_version = run.outputs[0].resource_name
        else:
            # NOTE: Skip if no input or output, so set an invalid API version
            api_version = ""

        protocol = activity.name.replace(" ", "")
        cmd = command.Command(api_version, protocol).with_metadata(
            "riffyn",
            {
                "experimentId": experiment_id,
                "activityId": run.activity_id,
                "runId": run.id,
            },
        )

        for input in activity.inputs:
            properties = {}
            for property in input.properties:
                header = f"{activity.id} | input | {input.id} | {property.id} | value"
                properties[utils.str_to_camelcase(property.name)] = datatable[header]

            cmd.spec[utils.str_to_camelcase(input.name)] = properties

        return cmd

    def __get_experiment_data_raw(self, experiment_id, activity_id, run):
        resp = requests.get(
            f"https://api.app.riffyn.com/v1/experiment/{experiment_id}/step/{activity_id}/data/raw",
            headers={"api-key": cfg.API_KEY},
            params={
                "rgid": [run.group_id],
                "rid": [run.id],
                "rnum": [run.num],
            },
        )
        resp.raise_for_status()
        return resp.json()
