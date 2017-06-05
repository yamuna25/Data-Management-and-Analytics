# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:05:30 2017

@author: Yamuna
"""

from elasticsearch import Elasticsearch
 
trip_i=[]
result2=[]
result3=[]
busname=[]
stop_i=[]

es = Elasticsearch(['ec2-52-27-28-3.us-west-2.compute.amazonaws.com:9200'])

result=es.search(index="bustracks", doc_type="trips", 
                 body={"query": {"match_phrase": { "trip_headsign": "1 SPRING GARDEN TO MUMFORD"}}})

print("\n%d documents found in trips table for Bus Name \"1 SPRING GARDEN TO MUMFORD\" \n" % result['hits']['total'])


print "\n"

result1 = es.search(index="bustracks", doc_type="trips", 
                    body={"query": {"match": {"route_id": "1-114"}}})
print("%d documents found in trips table for route_id 1-114\n" % result1['hits']['total'])


for doc in result1['hits']['hits']:
    if(doc['_source']['trip_headsign'] == "1 SPRING GARDEN TO MUMFORD" ):
    #print("%s) %s" % (doc['_id'], doc['_source']['trip_id']))
        trip_i.append(doc['_source']['trip_id'])


for i in trip_i:
    result2.append(es.search(index="bustracks", doc_type="stoptimes", 
                             body={"query": {"match": {"trip_id": '"'+i+'"'}}}))
    print i
    
print "\n"
for record in result2:
    for doc in record['hits']['hits']:
        print("%d of documents found for matching stop and route ids mentioned above" %(record['hits']['total']))
        #print("%s) %s" % (doc['_id'], doc['_source']['stop_id']))
        break
print "\n Stop_id :\n"

for record in result2:
    for doc in record['hits']['hits']:    
        stop_i.append(doc['_source']['stop_id'])

for i in stop_i:
    print i
    result3.append(es.search(index="bustracks", doc_type="stops", 
                             body={"query": {"match": {"stop_id": ''+i+''}}}))
    
print "\n name_stop/Stop Name :\n"
for record in result3:
    for doc in record['hits']['hits']:    
        print("%s" %  doc['_source']['name'])
    
