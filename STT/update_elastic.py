from STT.read_from_mongo import STT
from elastic.elastic_base import ElasticBase
from logger.logger import Logger
logger = Logger.get_logger()


class UpdateElastic:
    def __init__(self):
        logger.info("init update elastic")
        logger.info("elastic connect ok")
        self.es = ElasticBase()
        logger.info("speach_to_text connect ok")
        self.stt = STT()
    def update_elastic(self):
        logger.info("update elastic for each id")
        try:
            for doc in self.stt.speach_to_text():
                self.es.update_doc(doc["id"], doc["text"])
                logger.info(f"{doc['id']} is updated")
        except Exception as e:
            logger.error(f"can not update elastic: {e}")
