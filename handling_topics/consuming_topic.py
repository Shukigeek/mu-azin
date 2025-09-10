from services.elastic.elastic_base import ElasticBase
from services.mongo.write_read_mongo import Mongo
from services.kafka_pub_sub.sub.consumer import Consumer
from services.kafka_pub_sub.pub.producer import Producer
from hashlib import sha256
from bson.binary import Binary
from services.logger.logger import Logger

logger = Logger.get_logger(index="handel-topic-logs")


class Manager:
    def __init__(self, topic="podcasts", new_topic="audio-to-text"):
        self.topic = topic
        self.new_topic = new_topic
        self.consumer = Consumer(self.topic)
        self.producer = Producer()
        self.es = ElasticBase()
        self.mongo = Mongo()
    @staticmethod
    def read_bite_from_audio(self, path, ID, name):
        with open(fr"{path}", "rb") as f:
            logger.info("converting file to bytes!!!!!!")
            wav_data = f.read()
        # Store the binary data
        logger.info("creating a document to insert to mongodb")
        document = {"_id": ID, "filename": name, "data": Binary(wav_data)}
        return {"document": document}

    def read_from_kafka_saving_elastic_mongo(self):
        logger.info("Reading from Kafka saving to elastic and to mongo")
        self.es.wait_for_es()
        self.es.create_index()
        for event in self.consumer.consumer:
            logger.info("hi from consumer")
            if event.topic == self.topic:
                logger.info(f"topic {event.topic} received")
                name = event.value["meta data"]["File name"]
                # I cut it short because it was too long
                hash_id = sha256(name.encode()).hexdigest()[:8]
                logger.info(f"indexing the value of the data that came from kafka")
                self.es.index_doc({"metadata": event.value["meta data"]}, hash_id)
                try:
                    logger.info(f"sanding the actual audio file to a mongodb database")
                    document = self.read_bite_from_audio(self,event.value["path"], hash_id, name)["document"]
                    logger.info(document)
                    self.mongo.write(document)
                    # sanding to kafka the id of the document the inserted already to mongo
                    self.producer.publish_message(self.new_topic, {"id": hash_id})
                except Exception as e:
                    logger.error(f"mongo can't store that data: {e}")
            else:
                logger.error("topic not found")
