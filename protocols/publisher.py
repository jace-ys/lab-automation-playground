import json
import uuid

import click
import redis


@click.command("publish")
@click.argument("file")
@click.option(
    "--url",
    help="URL of the redis server.",
    default="redis://127.0.0.1:6389",
    show_default=True,
)
def publish(file, url):
    with open(file, "r") as f:
        protocol = json.loads(f.read())

        metadata = {
            "spec": {
                "experimentId": "123",
                "runId": "abc",
            }
        }

        if isinstance(protocol["spec"], list):
            metadata["spec"] = [
                {
                    "experimentId": "123",
                    "runId": "abc",
                }
            ]

        data = {
            **protocol,
            **{
                "uuid": uuid.uuid4().hex[:16],
                "metadata": {
                    "source": "test",
                    **metadata,
                },
            },
        }

        publisher = redis.StrictRedis.from_url(url)
        publisher.publish(data["apiVersion"], json.dumps(data))


if __name__ == "__main__":
    publish()
