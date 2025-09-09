from STT.read_from_mongo import STT
from logger.logger import Logger
logger = Logger.get_logger()


logger.info("starting app update elastic")
update = STT()
logger.info("updating elastic")
update.speach_to_text()