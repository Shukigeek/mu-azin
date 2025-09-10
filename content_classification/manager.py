from services.elastic.elastic_base import ElasticBase
from content_classification.data_anylsist import AnalyzeText
from services.kafka_pub_sub.sub.consumer import Consumer
from services.logger.logger import Logger

logger = Logger.get_logger(index="analysis-logs")


class Manager:
    def __init__(self, topic="text"):
        self.topic = topic
        self.consumer = Consumer(self.topic)
        self.es = ElasticBase()

    def add_fields(self):
        logger.info("getting id from topic text on kafka")
        for event in self.consumer.consumer:
            if event.topic == self.topic:
                logger.info(f"{event.topic}")
                try:
                    logger.info("adding new filed to elastic base un text hostility")
                    doc_id = event.value["id"]
                    text = self.es.search_by_id(doc_id)["_source"]["metadata"]["text"]
                    logger.info(text)
                    analyzer = AnalyzeText(text)
                    logger.info(analyzer.bds_precent)
                    self.es.update_doc_by_id(doc_id, {"doc": {"metadata": {"bds_precent": analyzer.bds_precent}}})
                    self.es.update_doc_by_id(doc_id, {"doc": {"metadata": {"is_bds": analyzer.is_bds()}}})
                    self.es.update_doc_by_id(doc_id,
                                             {"doc": {"metadata": {"bds_threat_level": analyzer.bds_threat_level()}}})
                except Exception as e:
                    logger.error(f"cannot update elastic: {e}")
