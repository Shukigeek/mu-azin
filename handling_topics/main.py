from handling_topics.consuming_topic import Manager
from services.logger.logger import Logger

logger = Logger.get_logger()

"""
creating a unique id based on the file name (hash)
and dividing it to two parts 
the metadata is sand it to index in elasticsearch 
and the path + the actual audio data it sands to
restored in mongo db in database called mu'azins
in a collection called audio files
"""
logger.info("creating an instants of handling_topics.consuming_topic => Manager")
m = Manager()
logger.info("handling data from main")
m.read_from_kafka_saving_elastic_mongo()
logger.info("data handel successfully")
