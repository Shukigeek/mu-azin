import os
from pymongo import MongoClient, errors
from logger.logger import Logger
logger = Logger.get_logger()

class Connection:
    def __init__(self):
        logger.info("initializing mongo client")
        self.host = os.getenv("MONGO_HOST","mongodb")
        self.port = os.getenv("MONGO_PORT","27017")
        self.db = os.getenv("MONGO_DB","mu'azins")
        self.auth = os.getenv("MONGO_AUTH_DB","admin")
        self.client = None

    def connect(self):
        try:
            logger.info("connecting to mongo db")
            self.client = MongoClient(
                host=self.host,
                port=int(self.port),
                authSource=self.auth,
                serverSelectionTimeoutMS=5000
            )
            self.client.server_info()
            logger.info("MongoDB connected successfully")
            return self.client
        except errors.ServerSelectionTimeoutError as e:
            logger.error("Failed to connect to MongoDB:", e)
            return None
        except errors.OperationFailure as e:
            logger.error("Authentication failed:", e)
            return None

    def close(self):
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")
