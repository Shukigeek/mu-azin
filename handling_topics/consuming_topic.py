from elastic.elastic_base import ElasticBase
from mongo.write_to_mongo import WriteToMongo
from kafka_pub_sub.sub.consumer import Consumer
from hashlib import sha256


class Manager:
    def __init__(self,topic="podcasts"):
        self.topic = topic
        self.consumer = Consumer(self.topic)
        self.es = ElasticBase()
        self.mongo = WriteToMongo()
    def read_from_kafka_saving_elastic_mongo(self):
        self.es.wait_for_es()
        self.es.create_index()
        for event in self.consumer.consumer:
            if event.topic == self.topic:
                name = event.value["meta data"]["File name"]
                hash_id = sha256(name.encode()).hexdigest()
                self.es.index_doc(event.value["meta data"],hash_id)
                try:
                    self.mongo.write(event.value["path"],name,hash_id)
                except Exception as e:
                    print(f"mongo can't store that data: {e}")



