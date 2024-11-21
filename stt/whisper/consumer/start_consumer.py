import logging
import os

# only root handler log to console
logging.basicConfig(level=logging.INFO)
for handler in logging.root.handlers:
    handler.addFilter(logging.Filter("root"))

# read env
queue_type = os.getenv("queue_type")
config = {
    "queue_type": queue_type,
    "queue_name": os.getenv("queue_name"),
    "host": os.getenv("host"),
    "port": os.getenv("port"),
    "username": os.getenv("username"),
    "password": os.getenv("password"),
}


logging.info(f"queue type:{queue_type}")
logging.debug(f"queue info: {config}")

# 开启队列消费者进行监听
match queue_type:
    case "rabbitmq":
        raise TypeError("rabbitmq 暂未实现")
    case "kafka":
        from kafka_handle import run_consumer

        logging.info("开始kafka消费\n")
        run_consumer(config)
    case _:
        raise TypeError("不支持的队列类型，目前仅支持 rabbitmq")
