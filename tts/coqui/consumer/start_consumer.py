import logging

# TODO 从已安装中导入
from message_queue_utils.rabbitmq import RabbitmqQueue
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

# only root handler log to console
logging.basicConfig(level=logging.INFO)
for handler in logging.root.handlers:
    handler.addFilter(logging.Filter("root"))


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
        logging.info("info: coqui_tts exe cmd")


# use
rabbitmq: RabbitmqQueue = CustomRabbitmqQueue(
    queue_name="hello",
    host="",
    port=10043,
    username="",
    password="",
)
rabbitmq.consumer()
