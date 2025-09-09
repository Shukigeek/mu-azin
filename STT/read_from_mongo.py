from kafka_pub_sub.pub.producer import Producer
from kafka_pub_sub.sub.consumer import Consumer
from STT.audio_to_text import AudioToText
from mongo.write_read_mongo import AudioToMongo
from elastic.elastic_base import ElasticBase
from logger.logger import Logger
logger = Logger.get_logger()
from io import BytesIO



class STT:
    def __init__(self,topic="audio-to-text"):
        self.es = ElasticBase()
        self.mongo = AudioToMongo()
        self.topic = topic
        self.producer = Producer()
        self.consumer = Consumer(topic)

    def speach_to_text(self):
        try:
            for record in self.mongo.read_all_from_mongo():
                id = record["_id"]
                data = record["data"]
                # refer to it like a file
                speach = AudioToText(BytesIO(data))
                logger.info("converting audio to text")
                text = speach.convert_audio()
                logger.info(f"publishing {self.topic} to kafka")
                self.producer.publish_message(self.topic,{"text":text})

        except Exception as e:
            logger.error(f"error fetching data from mongodb : {e}")

    def get_text_from_kafka(self):
        for event in self.consumer.consumer:
            if event.topic == self.topic:
                logger.info(f"consuming {self.topic} massage and updating elastic")
                self.es.update_doc_by_id(id, {"doc": {"metadata":{"text": event.value["text"]}}})




