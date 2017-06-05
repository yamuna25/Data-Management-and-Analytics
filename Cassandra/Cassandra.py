# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 17:56:20 2017

@author: Yamuna
"""

import web
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

urls = (
    '/(.*)', 'Cassandra'
)


class Cassandra:        
    def GET(self,option):
        ap = PlainTextAuthProvider(username='iccassandra', password='1826221e939359272d4bb9852cebe771')
        nodes = ['35.167.162.91', '35.167.225.2', '52.34.77.202']
        cluster = Cluster(nodes, auth_provider=ap)
        session = cluster.connect('keyspace1')
        if not option:
            return "give options - crime|hour|year|combined"
        if option == 'crime':
            result_crime_type = session.execute("SELECT json * FROM keyspace1.crime where text_general_code = 'Rape' allow filtering;")
            #for row in result_crime_type:
             #   return row.dc_key, row.ucr_general, row.location_block, row.month
            return result_crime_type
        if option == 'hour':
            result_hour = session.execute("SELECT * FROM keyspace1.crimeinc where hour >= 6 and hour <= 18 allow filtering;")
            for row in result_hour:
                return row.dc_key, row.ucr_general, row.location_block, row.month
        if option == 'year':
            result_year_month = session.execute("SELECT * FROM keyspace1.crimeinc where month = '2015-10' allow filtering;")
            for row in result_year_month:
                return row.dc_key, row.ucr_general, row.location_block, row.month
        if option =='combined':
            combined_result =  session.execute("SELECT * FROM keyspace1.crimeinc where text_general_code = 'Rape' and month = '2015-10' and hour >= 6 and hour <= 18 allow filtering;")
            return combined_result
            #for row in combined_result:
              #  return row.dc_key, row.ucr_general, row.location_block, row.month
               
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()