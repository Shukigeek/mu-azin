from STT.update_elastic import UpdateElastic
from logger.logger import Logger
logger = Logger.get_logger()


logger.info("starting app update elastic")
update = UpdateElastic()
logger.info("updating elastic")
update.update_elastic()