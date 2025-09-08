import time
import os
from elasticsearch import Elasticsearch, helpers
from logger.logger import Logger
logger = Logger.get_logger()


class ElasticBase:
    def __init__(self, index_name="mu-azin"):
        self.es = Elasticsearch(f"http://{os.getenv('ES_HOSTS')}:9200")
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

    def update_doc(self,document_id,update_body):
        try:
            response = self.es.update(index=self.index, id=document_id, body=update_body)
            logger.info(f"Document with ID {document_id} updated successfully.")
            logger.info(f"Response from elasticsearch: {response}")
        except Exception as e:
            logger.error(f"Error updating document: {e}")
    def return_all_docs(self):
        return self.es.search(index=self.index)
