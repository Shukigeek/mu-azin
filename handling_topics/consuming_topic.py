from elastic.elastic_base import ElasticBase
from mongo.write_read_mongo import AudioToMongo
from kafka_pub_sub.sub.consumer import Consumer
from hashlib import sha256
from bson.binary import Binary
from logger.logger import Logger
logger = Logger.get_logger()

class Manager:
    def __init__(self,topic="podcasts"):
        self.topic = topic
        self.consumer = Consumer(self.topic)
        self.es = ElasticBase()
        self.mongo = AudioToMongo()
    def read_bite_from_audio(self,path,ID,name):
        with open(path, "rb") as f:
            wav_data = f.read()
        # Store the binary data
        logger.info("creating a document to insert to mongodb")
        document = {"_id":ID,"filename": name, "data": Binary(wav_data)}
        return {"document":document}
    def read_from_kafka_saving_elastic_mongo(self):
        logger.info("Reading from Kafka saving to elastic and to mongo")
        self.es.wait_for_es()
        self.es.create_index()
        for event in self.consumer.consumer:
            if event.topic == self.topic:
                logger.info(f"topic {event.topic} received")
                name = event.value["meta data"]["File name"]
                # I cut it short because it was too long
                hash_id = sha256(name.encode()).hexdigest()[:8]
                logger.info(f"indexing the value of the data that came from kafka")
                self.es.index_doc(event.value["meta data"],hash_id)
                try:
                    logger.info(f"sanding the path to a mongodb database")
                    document = self.read_bite_from_audio(event.value["path"],hash_id,name)["document"]
                    self.mongo.write(document)
                except Exception as e:
                    logger.error(f"mongo can't store that data: {e}")




