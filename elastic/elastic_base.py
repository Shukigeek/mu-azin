import time
import os
from elasticsearch import Elasticsearch, helpers
from logger.logger import Logger
logger = Logger.get_logger()


class ElasticBase:
    def __init__(self, host=None, index_name="mu-azin"):
        logger.info(f"ElasticBase host: {host or "http://localhost:9200"}")
        self.es = Elasticsearch(os.getenv("ELASTICSEARCH_HOSTS", host or "http://localhost:9200"))
        logger.info(f"ElasticBase index name: {index_name}")
        self.index = index_name

    def wait_for_es(self):
        while True:
            logger.info(f"Waiting for ElasticSearch index: {self.index}")
            if self.es.ping():
                print("Elasticsearch is up!")
                logger.info("ElasticSearch is up!")
                break
            print("Waiting for Elasticsearch...")
            logger.info("Waiting for Elasticsearch...")
            time.sleep(2)

    def create_index(self):
        if not self.es.indices.exists(index=self.index):
            logger.info(f"Creating index: {self.index}")
            self.es.indices.create(index=self.index)
            print(f"Created index '{self.index}'")
    def index_doc(self,doc,ID):
        logger.info(f"Indexing doc: {doc}, id: {ID}")
        self.es.index(index=self.index, id=ID,body=doc)
        logger.info(f"refreshing index in elasticsearch")
        self.es.indices.refresh(index=self.index)


