from content_classification.manager import Manager
from services.logger.logger import Logger

logger = Logger.get_logger(index="analysis-logs")

m = Manager()
logger.info("adding fields to elastic")
m.add_fields()
