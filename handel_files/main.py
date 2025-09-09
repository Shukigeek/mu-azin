from handel_files.sand_to_kafka import Manager
from logger.logger import Logger
logger = Logger.get_logger()



# sanding data to kafka

logger.info("creating a instants of handel_files.sand_to_kafka => Manager")
m = Manager()
logger.info("producing data to kafka by topic from main")
m.produce_to_kafka()
logger.info("data produce successfully")