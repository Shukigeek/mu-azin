from mongo.mongo_dal import Connection
from bson.binary import Binary
from logger.logger import Logger
logger = Logger.get_logger()
import os

class WriteToMongo:
    def __init__(self):
        logger.info("connecting to mongodb")
        self.conn = Connection()
        self.client = self.conn.connect()
        logger.info("connected to mongodb database = {}".format(self.conn.db))
        self.db = self.client[os.getenv("MONGO_DB","mu'azins")]
        logger.info("creating collection 'audio files'")
        self.collection = self.db["audio files"]
    def write(self, path,name,ID):
        logger.info("writing a audio file in bites to mongodb")
        with open(path, "rb") as f:
            wav_data = f.read()

        # Store the binary data
        logger.info("creating a document to insert to mongodb")
        document = {"_id":ID,"filename": name, "data": Binary(wav_data)}
        self.collection.insert_one(document)
        logger.info("file {name} inserted to mongodb".format(name=name))


