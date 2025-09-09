from elastic.elastic_base import ElasticBase
from content_classification.data_analsist import AnalyzeText



class Manager:
    def __init__(self):
        self.es = ElasticBase()
        self.analyzer = AnalyzeText()

    def add_field_bulk(self, docs, field_name, func):
        actions = []
        for doc in docs:
            doc_id = doc["_id"]
            text = doc["_source"]["text"]
            new_value = func(text)
            actions.append({
                "_op_type": "update",
                "_index": self.es.index,
                "_id": doc_id,
                "doc": {field_name: new_value}
            })
        self.es.es.bulk_update(actions)
    def add_fields(self):
        data = self.es.return_all_docs()
        self.add_field_bulk(data,"bds_precent",self.analyzer.bds_precent)
        self.add_field_bulk(data,"is_bds",self.analyzer.is_bds())
        self.add_field_bulk(data,"bds_threat_level",self.analyzer.bds_threat_level())
