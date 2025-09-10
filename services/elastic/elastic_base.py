import time
import os
from elasticsearch import Elasticsearch
from services.logger.logger import Logger

logger = Logger.get_logger(index="elastic-logs")


class ElasticBase:
    def __init__(self, index_name="mu-azin"):
        self.es = Elasticsearch(f"http://{os.getenv('ES_HOSTS', 'elasticsearch')}:9200")
        self.index = index_name

    def wait_for_es(self):
        while True:
            logger.info(f"Waiting for ElasticSearch index: {self.index}")
            if self.es.ping():
                logger.info("ElasticSearch is up!")
                break
            logger.info("Waiting for Elasticsearch...")
            time.sleep(2)

    def create_index(self):
        if not self.es.indices.exists(index=self.index):
            logger.info(f"Creating index: {self.index}")
            self.es.indices.create(index=self.index)

    def index_doc(self, doc, ID):
        logger.info(f"Indexing doc: {doc}, id: {ID}")
        self.es.index(index=self.index, id=ID, body=doc)
        self.es.indices.refresh(index=self.index)

    def update_doc_by_id(self, document_id, update_body):
        try:
            self.es.update(index=self.index, id=document_id, body=update_body)
            logger.info(f"Document with ID {document_id} updated successfully.")
        except Exception as e:
            logger.error(f"Error updating document: {e}")

    def return_all_docs(self):
        return self.es.search(index=self.index)

    def search_by_id(self, doc_id):
        return self.es.get(index=self.index, id=doc_id)

    def search_kay_word(self,line,word):
        query = {
            "query": {
                "match": {
                    line: word
                }
            }
        }
        return self.es.search(index=self.index, body=query)

    def search_sentence(self,line,phrase):
        query = {
            "query": {
                "match_phrase": {
                    line: phrase
                }
            }
        }
        return self.es.search(index=self.index, body=query)
