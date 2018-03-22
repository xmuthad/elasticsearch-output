import sys
from datetime import datetime
from elasticsearch import Elasticsearch


hosts = ['3.1.6.53']
"""
hosts=["host1", "host2"]
maxsize is the connnection to each node.By default
we allow urllib3 to open up to 10 connections to each node.

"""
ES = None
LIMIT = 10000
def get_elastic():
    global ES
    if not ES:
        ES = Elasticsearch(hosts,
                           http_compress=True)
    return ES

def multi_get():
    es = get_elastic()
    #health_status = es.cluster.health()
    #print health_status
    #res = es.mget(params)
    #body = {"query":{"term":{}}}

    #number = es.count(body=body) 
    from_ = 0
    body = """
        {"index":["log-2018.03.21"]}
        {"query":{"match_all":{}},"from":%(from_)d, "size":%(limit)d}
        """ % dict(from_=from_, limit=LIMIT)
    res = es.msearch(body, doc_type='message')
    total = res['responses'][0]['hits']['total']
    hits = res['responses'][0]['hits']['hits']
    for i in xrange(total/LIMIT):
        body = """
            {"index":["log-2018.03.21"]}
            {"query":{"match_all":{}},"from":LIMIT*(1+i), "size":LIMIT}"""
        res = es.msearch(body, doc_type='message')
        hits.append(hits)
    print sys.getsizeof(hits)
    print len(hits)
multi_get()
