from services.elastic.elastic_base import ElasticBase
from services.logger.logger import Logger

logger = Logger.get_logger(index="endpoint-logs")


class GetQuerys:
    def __init__(self,query):
        self.es = ElasticBase()
        self.query = str(query)
    def search_index_word(self,line="metadata.text"):
        logger.info("collecting matching doc in elasticsearch")
        res = []
        for i in self.es.search_kay_word(line,self.query)["hits"]["hits"]:
            res.append(
                {"score": i["_source"]["score"],
                 "name": i["_source"]["metadata"]["name"],
                 "text": i["_source"]["metadata"]["text"]}
            )
        return res
    def search_index_phrase(self,line="metadata.text"):
        logger.info("collecting matching phrase in elasticsearch")
        res = []
        for i in self.es.search_sentence(line,self.query)["hits"]["hits"]:
            res.append(
                {"score": i["_source"]["score"],
                 "name": i["_source"]["metadata"]["name"],
                 "text": i["_source"]["metadata"]["text"]}
            )
        return res
    def results(self):
        if len(self.query.split()) > 1:
            return self.search_index_phrase()
        else:
            return self.search_index_word()
    def get_dbs_classification(self,line="is_bds"):
        logger.info("getting all data and group it by dbs attachment")
        is_bds = []
        for i in self.es.search_kay_word(line,"True")["hits"]["hits"]:
            is_bds.append(
                {"score": i["_source"]["score"],
                 "name": i["_source"]["metadata"]["name"],
                 "text": i["_source"]["metadata"]["text"]}
            )
            not_bds = []
            for i in self.es.search_kay_word(line, "False")["hits"]["hits"]:
                not_bds.append(
                    {"name": i["_source"]["metadata"]["name"]}
                )

        return {"is_dbs":is_bds,"not_bds": not_bds}