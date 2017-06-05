# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 21:16:46 2017

@author: Yamuna
"""

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import time

ap = PlainTextAuthProvider(username='iccassandra', password='1826221e939359272d4bb9852cebe771')

nodes = ['35.167.162.91', '35.167.225.2', '52.34.77.202']
cluster = Cluster(nodes, auth_provider=ap)

crime_type = raw_input("Enter the Crime types to be fetched (Thefts|Rape|Fraud): ")

session = cluster.connect('keyspace1')

count=0
### Query 1
start = time.time()
result_crime_type = session.execute("SELECT * FROM keyspace1.crime where text_general_code = '"+crime_type+"' allow filtering;")
end = time.time()
dur=end-start
print "Execution time: "
print dur
print "Printing 10 sample results:\n"
for row in result_crime_type:
    print row.dc_key, row.ucr_general, row.location_block, row.month
    count=count+1
    if count == 10:
        break
    
count = 0
### Query 2    
hour = raw_input("Enter time for crimes to be fetched(day|night|early_morning): ")
if hour =='day':
    start = time.time()
    result_hour = session.execute("SELECT * FROM keyspace1.crimeinc where hour >= 6 and hour <= 18 allow filtering;")
    end = time.time()
if hour =='night':
    start = time.time()
    result_hour = session.execute("SELECT * FROM keyspace1.crimeinc where hour <= 6 allow filtering;")
    end = time.time()
if hour =='early_morning':
    start = time.time()
    result_hour = session.execute("SELECT * FROM keyspace1.crimeinc where hour >= 18 allow filtering;")
    end = time.time()
    
dur=end-start
print "Execution time: "
print dur
print "\nPrinting 10 sample results:\n"
for row in result_hour:
    print row.dc_key, row.text_general_code, row.ucr_general, row.location_block, row.month
    count=count+1
    if count == 10:
        break
    
count = 0
### Query 3
year_month = raw_input("Enter the year-month for crimes to be fetched(2015-10|2009-05): ")
start = time.time()
result_year_month = session.execute("SELECT * FROM keyspace1.crimeinc where month = '"+year_month+"' allow filtering;")
end = time.time()

dur=end-start
print "Execution time: "
print dur

print "\nPrinting 10 sample results:\n"
for row in result_year_month:
    print row.dc_key, row.text_general_code, row.ucr_general, row.location_block, row.month
    count=count+1
    if count == 10:
        break

print ("\nCombining all the choices to make the combined query: \n")
count = 0
### Query 4
if hour =='day':
    start = time.time()
    combined_result =  session.execute("SELECT * FROM keyspace1.crimeinc where text_general_code = '"+crime_type+"' and month = '"+year_month+"' and hour >= 6 and hour <= 18 allow filtering;")
    end = time.time()
    
if hour =='night':
    start = time.time()
    combined_result =  session.execute("SELECT * FROM keyspace1.crimeinc where text_general_code = '"+crime_type+"' and month = '"+year_month+"' and hour <= 6 allow filtering;")
    end = time.time()

if hour =='early_morning':
    start = time.time()
    combined_result =  session.execute("SELECT * FROM keyspace1.crimeinc where text_general_code = '"+crime_type+"' and month = '"+year_month+"' and hour >= 18 allow filtering;")
    end = time.time()

dur=end-start
print "Execution time: "
print dur

print "\nPrinting 10 sample results:\n"
for row in combined_result:
    print row.dc_key, row.text_general_code, row.ucr_general, row.location_block, row.month
    count=count+1
    if count == 10:
        break



