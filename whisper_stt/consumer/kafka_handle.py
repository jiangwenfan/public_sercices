import logging

from kafka import KafkaConsumer


def run_consumer(config: dict):
    # username = config["username"]
    # password = config["password"]
    servers = f"{config['host']}:{config['port']}"

    bootstrap_servers = [servers]  # 根据实际情况修改
    topic_name = config["queue_name"]
    print(bootstrap_servers, topic_name)
    # 创建一个消费者，连接到指定的Kafka集群
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=bootstrap_servers,
        # auto_offset_reset="earliest",  # 从最早的消息开始读取
    )

    # 消费消息
    for message in consumer:
        logging.info(f"Received message: {message.value.decode('utf-8')}")

    # 不再需要消费消息时，关闭消费者
    consumer.close()
