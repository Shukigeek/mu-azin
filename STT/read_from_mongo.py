from services.kafka_pub_sub.pub.producer import Producer
from services.kafka_pub_sub.sub.consumer import Consumer
from STT.audio_to_text import AudioToText
from services.mongo.write_read_mongo import Mongo
from services.elastic.elastic_base import ElasticBase
from services.logger.logger import Logger

logger = Logger.get_logger(index="stt-logs")
from io import BytesIO


class STT:
    def __init__(self, topic="audio-to-text", new_topic="text"):
        self.es = ElasticBase()
        self.mongo = Mongo()
        self.topic = topic
        self.new_topic = new_topic
        self.producer = Producer()
        self.consumer = Consumer(topic)

    def speach_to_text(self, doc_id):
        try:
            doc = self.mongo.read_one_by_id(doc_id)
            data = doc["data"]

            # refer to it like a file
            speach = AudioToText(BytesIO(data))
            logger.info("converting audio to text")
            text = speach.convert_audio()
            logger.info(f"publishing {self.topic} to kafka")
            return text

        except Exception as e:
            logger.error(f"error fetching data from mongodb : {e}")

    def get_text_from_kafka(self):
        for event in self.consumer.consumer:
            if event.topic == self.topic:
                logger.info(f"consuming {self.topic} massage and updating elastic")
                doc_id = event.value["id"]
                text = self.speach_to_text(doc_id)
                logger.info(f"5 new text words = {text.split()[:5]}")
                self.es.update_doc_by_id(doc_id, {"doc": {"metadata": {"text": text}}})
                # updating topic in kafka what id in elastic have already the text
                self.producer.publish_message(self.new_topic, {"id": doc_id})
                logger.info("topic text sand to kafka----")

if __name__ == '__main__':
    from kafka import KafkaConsumer
    import json
    c = KafkaConsumer(
            "audio-to-text",
            group_id="muazin",
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=["127.0.0.1:9092"],
            auto_offset_reset='earliest'
        )
    for event in c:
        print(event.value)