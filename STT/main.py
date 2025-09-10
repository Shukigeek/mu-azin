from STT.read_from_mongo import STT
from services.logger.logger import Logger
logger = Logger.get_logger()


logger.info("starting app update elastic")
update = STT()
logger.info("updating elastic")
update.get_text_from_kafka()