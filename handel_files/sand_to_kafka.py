from handel_files.build_json import Json
from kafka_pub_sub.pub.producer import Producer
import os
from logger.logger import Logger
logger = Logger.get_logger()


class Manager:
    def __init__(self,topic="podcasts",path=None):
        logger.info(f"Initializing {topic}")
        self.topic = topic
        logger.info(f"initializing producer")
        self.producer = Producer()
        logger.info(f"initializing path by defaulter or inserted")
        self.path = path or "C:/podcasts"
    def produce_to_kafka(self):
        if self.path == "C:/podcasts":
            for i in range(1,34):
                logger.info(f"producing to topic {self.topic} un the file number {i}")
                self.producer.publish_message(self.topic,Json(f"{os.getenv('FILE_PATH','app/podcasts')}/download ({i}).wav").return_json())
                print(f"file number {i} path published on kafka")
        else:
            try:
                logger.info(f"producing to topic {self.topic} un a inserted file")
                self.producer.publish_message(self.topic,Json(f"{self.path}").return_json())
            except Exception as e:
                logger.error(f"path not valid: {e}")
                return f"path not valid: {e}"


