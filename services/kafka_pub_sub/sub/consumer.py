from kafka import KafkaConsumer
import json
import os
from services.logger.logger import Logger

logger = Logger.get_logger(index="kafka-logs")


class Consumer:
    def __init__(self, topic):
        logger.info('Consumer init')
        logger.info("kafka_broker_topic: {}".format(topic))
        kafka_broker = os.getenv("KAFKA_BROKER", "kafka:9092")
        logger.info("kafka consumer connected")
        self.consumer = KafkaConsumer(
            topic,
            group_id="muazin",
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=[kafka_broker],
            auto_offset_reset='earliest'
        )
