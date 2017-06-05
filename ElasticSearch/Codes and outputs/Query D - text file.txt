# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:05:30 2017

@author: Yamuna
"""

from elasticsearch import Elasticsearch
 
route_i=[]
result1=[]
result2=[]
result3=[]
busname=[]
stop_i=[]
hits = 0
final_route=""
count=0
trip_i=["6519227-2012_05M-1205BRsu-Sunday-02",
"6519225-2012_05M-1205BRsu-Sunday-02",
"6519224-2012_05M-1205BRsu-Sunday-02",
"6519219-2012_05M-1205BRsu-Sunday-02"
"6519217-2012_05M-1205BRsu-Sunday-02",
"6519214-2012_05M-1205BRsu-Sunday-02",
"6519209-2012_05M-1205BRsu-Sunday-02",
"6519206-2012_05M-1205BRsu-Sunday-02",
"6519205-2012_05M-1205BRsu-Sunday-02",
"6519202-2012_05M-1205BRsu-Sunday-02",
"6519200-2012_05M-1205BRsu-Sunday-02",
"6519198-2012_05M-1205BRsu-Sunday-02",
"6519197-2012_05M-1205BRsu-Sunday-02",
"6519195-2012_05M-1205BRsu-Sunday-02",
"6519189-2012_05M-1205BRsu-Sunday-02",
"6519187-2012_05M-1205BRsu-Sunday-02",
"6519186-2012_05M-1205BRsu-Sunday-02",
"6519184-2012_05M-1205BRsu-Sunday-02",
"6519183-2012_05M-1205BRsu-Sunday-02",
"6519178-2012_05M-1205BRsu-Sunday-02",
"6519175-2012_05M-1205BRsu-Sunday-02",
"6519172-2012_05M-1205BRsu-Sunday-02",
"6519171-2012_05M-1205BRsu-Sunday-02",
"6519170-2012_05M-1205BRsu-Sunday-02",
"6519169-2012_05M-1205BRsu-Sunday-02",
"6519166-2012_05M-1205BRsu-Sunday-02",
"6519164-2012_05M-1205BRsu-Sunday-02",
"6519153-2012_05M-1205BRsu-Sunday-02",
"6519152-2012_05M-1205BRsu-Sunday-02",
"6519149-2012_05M-1205BRsu-Sunday-02",
"6519148-2012_05M-1205BRsu-Sunday-02",
"6519143-2012_05M-1205BRsu-Sunday-02",
"6519140-2012_05M-1205BRsu-Sunday-02",
"6519139-2012_05M-1205BRsu-Sunday-02",
"6519137-2012_05M-1205BRsu-Sunday-02",
"6519136-2012_05M-1205BRsu-Sunday-02",
"6519132-2012_05M-1205BRsu-Sunday-02",
"6519131-2012_05M-1205BRsu-Sunday-02",
"6516902-2012_05M-1205BRsa-Saturday-02",
"6516901-2012_05M-1205BRsa-Saturday-02",
"6516898-2012_05M-1205BRsa-Saturday-02",
"6516895-2012_05M-1205BRsa-Saturday-02",
"6516891-2012_05M-1205BRsa-Saturday-02",
"6516889-2012_05M-1205BRsa-Saturday-02",
"6516887-2012_05M-1205BRsa-Saturday-02",
"6516886-2012_05M-1205BRsa-Saturday-02",
"6516885-2012_05M-1205BRsa-Saturday-02",
"6516875-2012_05M-1205BRsa-Saturday-02",
"6516869-2012_05M-1205BRsa-Saturday-02",
"6516865-2012_05M-1205BRsa-Saturday-02",
"6516863-2012_05M-1205BRsa-Saturday-02",
"6516861-2012_05M-1205BRsa-Saturday-02",
"6516859-2012_05M-1205BRsa-Saturday-02",
"6516858-2012_05M-1205BRsa-Saturday-02",
"6516856-2012_05M-1205BRsa-Saturday-02",
"6516855-2012_05M-1205BRsa-Saturday-02",
"6516852-2012_05M-1205BRsa-Saturday-02",
"6516851-2012_05M-1205BRsa-Saturday-02",
"6516845-2012_05M-1205BRsa-Saturday-02",
"6516843-2012_05M-1205BRsa-Saturday-02",
"6516842-2012_05M-1205BRsa-Saturday-02",
"6516840-2012_05M-1205BRsa-Saturday-02",
"6516837-2012_05M-1205BRsa-Saturday-02",
"6516835-2012_05M-1205BRsa-Saturday-02",
"6516833-2012_05M-1205BRsa-Saturday-02",
"6516832-2012_05M-1205BRsa-Saturday-02",
"6516829-2012_05M-1205BRsa-Saturday-02",
"6516818-2012_05M-1205BRsa-Saturday-02",
"6516813-2012_05M-1205BRsa-Saturday-02",
"6516812-2012_05M-1205BRsa-Saturday-02",
"6516808-2012_05M-1205BRsa-Saturday-02",
"6516804-2012_05M-1205BRsa-Saturday-02",
"6516803-2012_05M-1205BRsa-Saturday-02",
"6516796-2012_05M-1205BRsa-Saturday-02",
"6516794-2012_05M-1205BRsa-Saturday-02",
"6516793-2012_05M-1205BRsa-Saturday-02",
"6516791-2012_05M-1205BRsa-Saturday-02",
"6516789-2012_05M-1205BRsa-Saturday-02",
"6516788-2012_05M-1205BRsa-Saturday-02",
"6516787-2012_05M-1205BRsa-Saturday-02",
"6516786-2012_05M-1205BRsa-Saturday-02",
"6516785-2012_05M-1205BRsa-Saturday-02",
"6516784-2012_05M-1205BRsa-Saturday-02",
"6516781-2012_05M-1205BRsa-Saturday-02",
"6516779-2012_05M-1205BRsa-Saturday-02",
"6516775-2012_05M-1205BRsa-Saturday-02",
"6516774-2012_05M-1205BRsa-Saturday-02",
"6516773-2012_05M-1205BRsa-Saturday-02",
"6516771-2012_05M-1205BRsa-Saturday-02",
"6514214-2012_05M-1205BRwd-Weekday-02",
"6514212-2012_05M-1205BRwd-Weekday-02",
"6514211-2012_05M-1205BRwd-Weekday-02",
"6514204-2012_05M-1205BRwd-Weekday-02",
"6514203-2012_05M-1205BRwd-Weekday-02",
"6514201-2012_05M-1205BRwd-Weekday-02",
"6514200-2012_05M-1205BRwd-Weekday-02",
"6514195-2012_05M-1205BRwd-Weekday-02",
"6514194-2012_05M-1205BRwd-Weekday-02",
"6514192-2012_05M-1205BRwd-Weekday-02",
"6514191-2012_05M-1205BRwd-Weekday-02",
"6514190-2012_05M-1205BRwd-Weekday-02",
"6514188-2012_05M-1205BRwd-Weekday-02",
"6514185-2012_05M-1205BRwd-Weekday-02",
"6514183-2012_05M-1205BRwd-Weekday-02",
"6514182-2012_05M-1205BRwd-Weekday-02",
"6514181-2012_05M-1205BRwd-Weekday-02",
"6514180-2012_05M-1205BRwd-Weekday-02",
"6514174-2012_05M-1205BRwd-Weekday-02",
"6514173-2012_05M-1205BRwd-Weekday-02",
"6514166-2012_05M-1205BRwd-Weekday-02",
"6514164-2012_05M-1205BRwd-Weekday-02",
"6514163-2012_05M-1205BRwd-Weekday-02",
"6514158-2012_05M-1205BRwd-Weekday-02",
"6514154-2012_05M-1205BRwd-Weekday-02",
"6514153-2012_05M-1205BRwd-Weekday-02",
"6514151-2012_05M-1205BRwd-Weekday-02",
"6514149-2012_05M-1205BRwd-Weekday-02",
"6514145-2012_05M-1205BRwd-Weekday-02",
"6514144-2012_05M-1205BRwd-Weekday-02",
"6514143-2012_05M-1205BRwd-Weekday-02",
"6514142-2012_05M-1205BRwd-Weekday-02",
"6514139-2012_05M-1205BRwd-Weekday-02",
"6514136-2012_05M-1205BRwd-Weekday-02",
"6514129-2012_05M-1205BRwd-Weekday-02",
"6514127-2012_05M-1205BRwd-Weekday-02",
"6514125-2012_05M-1205BRwd-Weekday-02",
"6514122-2012_05M-1205BRwd-Weekday-02",
"6514121-2012_05M-1205BRwd-Weekday-02",
"6514120-2012_05M-1205BRwd-Weekday-02",
"6514119-2012_05M-1205BRwd-Weekday-02",
"6514118-2012_05M-1205BRwd-Weekday-02",
"6514116-2012_05M-1205BRwd-Weekday-02",
"6514114-2012_05M-1205BRwd-Weekday-02",
"6514110-2012_05M-1205BRwd-Weekday-02",
"6514108-2012_05M-1205BRwd-Weekday-02",
"6514101-2012_05M-1205BRwd-Weekday-02",
"6514100-2012_05M-1205BRwd-Weekday-02",
"6514099-2012_05M-1205BRwd-Weekday-02",
"6514098-2012_05M-1205BRwd-Weekday-02",
"6514095-2012_05M-1205BRwd-Weekday-02",
"6514094-2012_05M-1205BRwd-Weekday-02",
"6514092-2012_05M-1205BRwd-Weekday-02",
"6514091-2012_05M-1205BRwd-Weekday-02",
"6514090-2012_05M-1205BRwd-Weekday-02",
"6514088-2012_05M-1205BRwd-Weekday-02",
"6514084-2012_05M-1205BRwd-Weekday-02",
"6514079-2012_05M-1205BRwd-Weekday-02",
"6514078-2012_05M-1205BRwd-Weekday-02",
"6514077-2012_05M-1205BRwd-Weekday-02",
"6514074-2012_05M-1205BRwd-Weekday-02",
"6514073-2012_05M-1205BRwd-Weekday-02",
"6514072-2012_05M-1205BRwd-Weekday-02",
"6514067-2012_05M-1205BRwd-Weekday-02",
"6514066-2012_05M-1205BRwd-Weekday-02",
"6514064-2012_05M-1205BRwd-Weekday-02",
"6514063-2012_05M-1205BRwd-Weekday-02",
"6514062-2012_05M-1205BRwd-Weekday-02",
"6514061-2012_05M-1205BRwd-Weekday-02",
"6514059-2012_05M-1205BRwd-Weekday-02",
"6514057-2012_05M-1205BRwd-Weekday-02",
"6514056-2012_05M-1205BRwd-Weekday-02",
"6514055-2012_05M-1205BRwd-Weekday-02",
"6514049-2012_05M-1205BRwd-Weekday-02",
"6514048-2012_05M-1205BRwd-Weekday-02",
"6514043-2012_05M-1205BRwd-Weekday-02",
"6514042-2012_05M-1205BRwd-Weekday-02",
"6514040-2012_05M-1205BRwd-Weekday-02"
]

es = Elasticsearch(['ec2-52-27-28-3.us-west-2.compute.amazonaws.com:9200'])

result=es.search(index="bustracks", doc_type="trips", 
                 body={"query": {"wildcard" : { "route_id" : "*" }}})

for doc in result['hits']['hits']:
#    if(doc['_source']['trip_headsign'] == "1 SPRING GARDEN TO MUMFORD" ):
    #print("%s) %s" % (doc['_id'], doc['_source']['trip_id']))
    route_i.append(doc['_source']['route_id'])
    

for i in route_i:
    result2.append(es.search(index="bustracks", doc_type="trips", 
                 body={"query": {"match" : { "route_id" : '"'+i+'"' }}}))

for record in result2:
    for doc in record['hits']['hits']:
        print("%d of hits for route_id %s" %(record['hits']['total'],doc['_source']['route_id']))
        if hits<record['hits']['total']:
            hits = record['hits']['total']
            final_route=doc['_source']['route_id']
            #trip_i=doc['_source']['trip_id']
        break
print "Max number of hits: "
print hits
print "Route with Max hits: "+final_route

for i in trip_i:
    result1.append(es.search(index="bustracks", doc_type="stoptimes", 
                 body={"query": {"match" : { "trip_id" : '"'+i+'*"' }}}))
    
    #print("%d documents found - for Trip_id" % result1['hits']['total'])

print "Collecting stop ids"

for record in result1:
    for doc in record['hits']['hits']:
        stop_i.append(doc['_source']['stop_id'])
        #print("%d documents found" % record['hits']['total'])

print "Collecting top 3 busiest bus stop"

for i in stop_i:
    result3.append(es.search(index="bustracks", doc_type="stops", 
                 body={"query": {"match" : { "stop_id" : ''+i+'' }}}))

for record in result3:
    for doc in record['hits']['hits']:
        #print("%d documents found - for Stop_id" % record['hits']['total'])
        print("%d hits - Bus Stop names : %s" %(record['hits']['total'],doc['_source']['name']))
    count=count+1
    if count == 3:
        break

