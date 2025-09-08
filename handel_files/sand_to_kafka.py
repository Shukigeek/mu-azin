from handel_files.build_json import Json
from kafka_pub_sub.pub.producer import Producer

class Manager:
    def __init__(self,topic="podcasts"):
        self.topic = topic
        self.producer = Producer()
    def produce_to_kafka(self):
        for i in range(1,34):
            self.producer.publish_message(self.topic,Json(f"C:/Users/shuki/Desktop/kodkod/mu'azins/podcasts/download ({i}).wav").return_json())
            print(f"file number {i} path published on kafka")


