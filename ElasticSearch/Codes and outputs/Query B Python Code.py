# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:09:43 2017

@author: Yamuna
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:05:30 2017

@author: Yamuna
"""

from elasticsearch import Elasticsearch
 
trip_i=[]
result2=[]
busname=[]

es = Elasticsearch(['ec2-52-27-28-3.us-west-2.compute.amazonaws.com:9200'])

r1=es.search(index="bustracks", doc_type="stoptimes", 
                 body={"query": {"match_phrase": { "arrival_time": "13:00:00"}}})
print("%d documents found in stoptimes mapping for arrival time 13:00:00\n" % r1['hits']['total'])
r2=es.search(index="bustracks", doc_type="stoptimes", 
                 body={"query": {"match_phrase": { "arrival_time": "14:00:00"}}})
print("%d documents found in stoptimes mapping for arrival time 14:00:00\n" % r2['hits']['total'])
r3=es.search(index="bustracks", doc_type="stoptimes", 
                 body={"query": {"match_phrase": { "arrival_time": "15:00:00"}}})
print("%d documents found in stoptimes mapping for arrival time 15:00:00\n" % r3['hits']['total'])

for doc in r1['hits']['hits']:
    trip_i.append(doc['_source']['trip_id'])

for doc in r2['hits']['hits']:
    trip_i.append(doc['_source']['trip_id'])

for doc in r3['hits']['hits']:
    trip_i.append(doc['_source']['trip_id'])
    
for i in trip_i:
    result2.append(es.search(index="bustracks", doc_type="trips", 
                             body={"query": {"match": {"trip_id": '"'+i+'"'}}}))
print "\n"
for record in result2:
    for doc in record['hits']['hits']:
        print("%d of documents found for each trip_id" %(record['hits']['total']))
        break
print "\n Trip_id :\n"

for record in result2:
    for doc in record['hits']['hits']:    
        print("%s" %  doc['_source']['trip_id'])
        break
print "\n Trip_headsign/Bus Name :\n"
for record in result2:
    for doc in record['hits']['hits']:    
        print("%s" %  doc['_source']['trip_headsign'])

