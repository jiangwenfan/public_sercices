import logging

from common_packages.message_queue_utils import RabbitmqQueue
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties


# overwrite
class CustomRabbitmqQueue(RabbitmqQueue):
    def message_callback(
        self,
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes,
    ) -> None:
        # TODO handle core
        logging.info(f"info: consumer handle ok: {body.decode()}")
        logging.info("info: whisper exe cmd")


def run_cnsumer(config: dict):
    rabbitmq: RabbitmqQueue = CustomRabbitmqQueue(
        queue_name=config["queue_name"],
        host=config["host"],
        port=config["port"],
        username=config["username"],
        password=config["password"],
    )
    rabbitmq.consumer()
