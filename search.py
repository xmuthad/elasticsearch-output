import sys
from datetime import datetime
from elasticsearch import Elasticsearch


hosts = ['3.1.6.53']
"""
hosts=["host1", "host2"]
maxsize is the connnection to each node.By default
we allow urllib3 to open up to 10 connections to each node.

"""
LIMIT = 10000


class Search(object):

    def __init__(self):
        self.es = Elasticsearch(hosts,
                               http_compress=True)
    
    def multi_get(self):
        #health_status = es.cluster.health()
        #print health_status
        #res = es.mget(params)
        #body = {"query":{"term":{}}}
    
        #number = es.count(body=body) 
        index = ["log-2018.03.21"] 
        from_ = 0
        body = """
            {"index":%(index)s}
            {"query":{"match_all":{}},"from":%(from_)d, "size":%(limit)d}
            """ % dict(index=index, from_=from_, limit=LIMIT)
        res = self.es.msearch(body, doc_type='message')
        total = res['responses'][0]['hits']['total']
        hits = res['responses'][0]['hits']['hits']
        for i in xrange(total/LIMIT):
            body = """
                {"index":["log-2018.03.21"]}
                {"query":{"match_all":{}},"from":LIMIT*(1+i), "size":LIMIT}"""
            res = es.msearch(body, doc_type='message')
            hits.append(hits)
        return hits
    
    def _count(self, index=None, item=None, value=None):
        body = {
            "query":{
                "term": {
                    item: value,
                }
            } 
        }
        res = self.es.count(index=index, body=body)
        return res['count']

class LogReport(Search):
     def __init__(self):
         super(LogReport, self).__init__()
     def converge_info(self):
         return self._count()

reporting = LogReport() 
end = reporting.converge_info()
print end
