from kafka import KafkaProducer

# Kafka集群的地址
bootstrap_servers = ["localhost:9092"]  # 根据实际情况修改
topic_name = "test123"

# 创建一个生产者，连接到指定的Kafka集群
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# 要发送的消息
message = b"Hello, Kafka!"

# 发送消息到指定的topic
producer.send(topic_name, message)

# 确保所有的消息都已经发送
producer.flush()

# 关闭生产者连接
producer.close()

print(f"Message '{message.decode('utf-8')}' sent to topic '{topic_name}'.")
