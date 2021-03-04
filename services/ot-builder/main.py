import uvicorn
from fastapi import FastAPI

from lib import log, redis
from lib.commands.subscriber import Subscriber
from src.config import config
from src.protocols.builder import ProtocolBuilder
from src.routers import builds

cfg = config.Config()
logger = log.Logger.new()
cache = redis.Client.connect(cfg.cache.ADDR)
pubsub = redis.Client.connect(cfg.pubsub.ADDR).pubsub()

app = FastAPI()
app.include_router(builds.router)


if __name__ == "__main__":
    builder = ProtocolBuilder(logger, cache, cfg.builder)
    subscriber = Subscriber(builder)

    try:
        pubsub.subscribe(**{cfg.pubsub.SUBSCRIPTION_TOPIC: subscriber.receive})
        pubsub_thread = pubsub.run_in_thread()  # TODO: Handle exception in thread
        logger.info("builder.subscribe.started", channel=cfg.pubsub.SUBSCRIPTION_TOPIC)

        logger.info("server.started", port=cfg.server.PORT)
        uvicorn.run(app, host=cfg.server.HOST, port=cfg.server.PORT)
        logger.info("server.stopped")

    except Exception as err:
        logger.error("service.fatal", error=err)

    except KeyboardInterrupt:
        pass

    finally:
        pubsub_thread.stop()
        logger.info("builder.subscribe.stopped")
