from read_recoreds.audio_to_text import AudioToText
from mongo.write_read_mongo import AudioToMongo
from elastic.elastic_base import ElasticBase
from logger.logger import Logger
logger = Logger.get_logger()



class STT:
    def __init__(self):
        logger.info("initialize STT")
        logger.info("connect to elastic")
        self.es = ElasticBase()
        logger.info("connect to mongodb")
        self.mongo = AudioToMongo()
    def speach_to_text(self):
        all_docs = []
        for record in self.mongo.read_all_from_mongo():
            id = record["_id"]
            data = record["data"]
            logger.info("connect to whisper")
            whisper = AudioToText(data)
            logger.info("converting audio to text")
            text = whisper.convert_audio()
            data = {"id": id, "text": text}
            all_docs.append(data)
        return all_docs