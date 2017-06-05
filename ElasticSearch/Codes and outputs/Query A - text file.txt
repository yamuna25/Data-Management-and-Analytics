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

result=es.search(index="bustracks", doc_type="stops", body={"query": {"match_phrase": { "name": "dartmouth Bridge Terminal - Bay 15"}}})
print("%d documents found in stopts table for name_stop dartmouth Bridge Terminal - Bay 15\n" % result['hits']['total'])
for doc in result['hits']['hits']:
    stop=doc['_source']['stop_id']
print " Stop_id: "+stop
print "\n"
result1 = es.search(index="bustracks", doc_type="stoptimes", body={"query": {"match": {"stop_id": "7615"}}})
print("%d documents found in stoptimes table for stop_id 7615\n" % result1['hits']['total'])
#print result1

for doc in result1['hits']['hits']:
    #print("%s) %s" % (doc['_id'], doc['_source']['trip_id']))
    trip_i.append(doc['_source']['trip_id'])
    
for i in trip_i:
    #print i
    result2.append(es.search(index="bustracks", doc_type="trips", body={"query": {"match": {"trip_id": '"'+i+'"'}}}))
    #print result2
    #print("%d documents found" % result2['hits']['total'])
print "\n"
for record in result2:
    for doc in record['hits']['hits']:
        print("%d of documents found for each trip_id" %(record['hits']['total']))
        #print("%s) %s" % (doc['_id'], doc['_source']['trip_headsign']))
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
    #busname.append(doc['_source']['trip_headsign'])
    #print busname

