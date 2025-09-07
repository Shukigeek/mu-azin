from elastic.elastic_base import ElasticBase
from mongo.write_to_mongo import WriteToMongo
from handel_files.build_json import Json
from kafka_pub_sub.pub.producer import Producer
from kafka_pub_sub.sub.consumer import Consumer
from hashlib import sha256


class Manager:
    def __init__(self,topic="podcasts"):
        self.topic = topic
        self.producer = Producer()
        self.consumer = Consumer(self.topic)
        self.es = ElasticBase()
        self.mongo = WriteToMongo()
    def produce_to_kafka(self):
        for i in range(1,34):
            self.producer.publish_message(self.topic,Json(f"C:/Users/shuki/Desktop/kodkod/mu'azins/podcasts/download ({i}).wav").return_json())
            print(f"file number {i} path published on kafka")
    def read_from_kafka_saving_elastic_mongo(self):
        self.es.wait_for_es()
        print("*****************")
        self.es.create_index()
        for event in self.consumer.consumer:
            if event.topic == self.topic:
                name = event.value["meta data"]["File name"]
                hash_id = sha256(name.encode()).hexdigest()
                self.es.index_doc(event.value["meta data"],hash_id)
                try:
                    self.mongo.write(event.value["path"],name,hash_id)
                except Exception as e:
                    return e

if __name__ == '__main__':
    m = Manager()
    m.produce_to_kafka()
    m.read_from_kafka_saving_elastic_mongo()
