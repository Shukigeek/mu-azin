from mongo.mongo_dal import Connection
from logger.logger import Logger
logger = Logger.get_logger()
import os

class AudioToMongo:
    def __init__(self):
        logger.info("connecting to mongodb")
        self.conn = Connection()
        self.client = self.conn.connect()
        logger.info("connected to mongodb database = {}".format(self.conn.db))
        self.db = self.client[os.getenv("MONGO_DB","mu'azins")]
        logger.info("creating collection 'audio files'")
        self.collection = self.db["audio files"]
    def write(self, document):
        self.collection.insert_one(document)
        logger.info("file inserted to mongodb")
    def read_all_from_mongo(self):
        logger.info("reading all audio files from mongodb")
        all_docs = self.collection.find({})
        return all_docs


