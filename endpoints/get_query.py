from services.elastic.elastic_base import ElasticBase



class GetQuerys:
    def __init__(self,query):
        self.es = ElasticBase()
        self.query = str(query)
    def search_index_word(self,line="text"):
        res = []
        for i in self.es.search_kay_word(line,self.query)["hits"]["hits"]:
            res.append(
                {"score": i["_source"]["score"],
                 "name": i["_source"]["meta data"]["name"],
                 "text": i["_source"]["meta data"]["text"]}
            )
        return res
    def search_index_phrase(self,line="text"):
        res = []
        for i in self.es.search_sentence(line,self.query)["hits"]["hits"]:
            res.append(
                {"score": i["_source"]["score"],
                 "name": i["_source"]["meta data"]["name"],
                 "text": i["_source"]["meta data"]["text"]}
            )
        return res
    def results(self):
        if len(self.query.split()) > 1:
            return self.search_index_phrase()
        else:
            return self.search_index_word()