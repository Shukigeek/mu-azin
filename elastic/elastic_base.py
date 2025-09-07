import os
import time
from elasticsearch import Elasticsearch, helpers
from hashlib import md5


class ElasticBase:
    def __init__(self, host=None, index_name="mu-azin"):
        self.es = Elasticsearch("http://localhost:9200")
        self.index = index_name

    def wait_for_es(self):
        while True:
            if self.es.ping():
                print("Elasticsearch is up!")
                break
            print("Waiting for Elasticsearch...")
            time.sleep(2)

    def create_index(self):
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index)
            print(f"Created index '{self.index}'")
    def index_doc(self,doc,ID):
        self.es.index(index=self.index, id=ID,body=doc)
        self.es.indices.refresh(index=self.index)


if __name__ == '__main__':
    e = ElasticBase()
    e.wait_for_es()

