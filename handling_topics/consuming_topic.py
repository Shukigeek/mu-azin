from elastic.elastic_base import ElasticBase
from mongo.write_to_mongo import WriteToMongo
from kafka_pub_sub.sub.consumer import Consumer
from hashlib import sha256
from logger.logger import Logger
logger = Logger.get_logger()

class Manager:
    def __init__(self,topic="podcasts"):
        logger.info("Initializing Manager")
        logger.info("Initializing Elastic")
        logger.info("Initializing Mongo")
        logger.info("Initializing Kafka consumer")
        logger.info("topic: {}".format(topic))
        self.topic = topic
        self.consumer = Consumer(self.topic)
        self.es = ElasticBase()
        self.mongo = WriteToMongo()
    def read_from_kafka_saving_elastic_mongo(self):
        logger.info("Reading from Kafka saving to elastic and to mongo")
        self.es.wait_for_es()
        self.es.create_index()
        for event in self.consumer.consumer:
            logger.info(f"waiting to {event.topic}")
            if event.topic == self.topic:
                logger.info(f"topic {event.topic} received")
                logger.info(f"gating the name of a file")
                name = event.value["meta data"]["File name"]
                logger.info(f"name: {name}")
                logger.info("creating a unique id by hashing the name")
                hash_id = sha256(name.encode()).hexdigest()
                logger.info(f"hash_id: {hash_id}")
                logger.info(f"indexing the value of the data that came from kafka")
                self.es.index_doc(event.value["meta data"],hash_id)
                try:
                    logger.info(f"sanding the path to a mongodb database")
                    self.mongo.write(event.value["path"],name,hash_id)
                except Exception as e:
                    logger.error(f"mongo can't store that data: {e}")
                    # print(f"mongo can't store that data: {e}")



