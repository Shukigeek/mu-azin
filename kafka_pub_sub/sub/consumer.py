from kafka import KafkaConsumer
import json
import os
class Consumer:
    def __init__(self, topic):
        kafka_broker = os.getenv("KAFKA_BROKER", "127.0.0.1:9092")
        self.consumer = KafkaConsumer(
            topic,
            group_id= "preprocess",
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=[kafka_broker],
            auto_offset_reset='earliest'
        )




