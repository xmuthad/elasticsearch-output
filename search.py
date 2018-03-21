from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

"""
hosts=["host1", "host2"]
maxsize is the connnection to each node.By default
we allow urllib3 to open up to 10 connections to each node.

"""
#es = Elasticsearch(hosts,
#                   maxsize=30,
#                   http_compress=True)
res = es.mget()
