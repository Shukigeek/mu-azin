from content_classification.manager import Manager
from logger.logger import Logger
logger = Logger.get_logger()

m = Manager()
logger.info("adding fields to elastic")
m.add_fields()