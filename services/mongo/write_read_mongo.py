from services.mongo.mongo_dal import Connection
from services.logger.logger import Logger

logger = Logger.get_logger(index="mongo-logs")
import os


class Mongo:
    def __init__(self):
        logger.info("connecting to mongodb")
        self.conn = Connection()
        self.client = self.conn.connect()
        logger.info("connected to mongodb database = {}".format(self.conn.db))
        self.db = self.client[os.getenv("MONGO_DB")]
        logger.info("creating collection 'audio files'")
        self.collection = self.db["audio files"]

    def write(self, document):
        self.collection.insert_one(document)
        logger.info("file inserted to mongodb")

    def read_one_by_id(self, doc_id):
        data = self.collection.find_one({"_id": doc_id})
        return data

    def read_all_from_mongo(self):
        logger.info("reading all audio files from mongodb")
        all_docs = self.collection.find({})
        return list(all_docs)


if __name__ == '__main__':
    a = Mongo()
    print(a.read_all_from_mongo())
