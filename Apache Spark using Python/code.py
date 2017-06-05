# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:23:04 2017

@author: Yamuna
"""

# importing packages
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
import re
import sys

# Getting the input arguments Name and Year

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Missing parameters\n")
        exit(-1)

    InName = sys.argv[1]

    InYear = sys.argv[2]

# Creating Spark Context
sc = SparkContext("local", "myapp")

# Create SQL Context

sqlc=SQLContext(sc)

# Reading text file into an RDD

wordRDD=sc.textFile("\\Users\\Yamuna\\Desktop\\Assignment3\\input\\WordCountData.txt")

# Performing RDD operations for wordcount
# Funtion to pre-process data, removing special characters using Regular expression and to lowercase
def stripContent(myline):
    return(re.sub('[^a-zA-Z0-9 ]+','', myline.lower()))

# Converting the sentences to individual tokens in the RDD and create a FlatMap
wordRDDtokens=wordRDD.flatMap(lambda lines:stripContent(lines).split())

# Counting distinct words in the document
                    
countDistWordRDD = wordRDDtokens.map(lambda word: (word,1))\
                    .reduceByKey(lambda w1,w2: w1+w2)

# Saving an RDDs to file


countDistWordRDD.saveAsTextFile("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\DistinctWordCount")

# Reading a csv file to DataFrame
# Schema can be predefined or inferred.Check the syntax from official python Spark documentation

childbirthDF=sqlc.read.format('com.databricks.spark.csv').options(header='true')\
            .load('\\Users\\Yamuna\\Desktop\\Assignment3\\input\\NationalNames.csv')

# Creating a view on DataFrame for Spark SQL operation
childbirthDF.createOrReplaceTempView("Births")

# Running SQL query
Births=sqlc.sql("Select * from Births")

# Saving DataFrame as JSON file

Births.write.save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\Births.json", format="json")

# Query 1 - Total number of birth registered in a year

sqlc.sql("Select Year, sum(Count) as NumberOfBirth from Births group by Year").show()

BirthbyYear=sqlc.sql("Select Year, sum(Count) as NumberOfBirth from Births group by Year")

BirthbyYear.write.\
    format("com.databricks.spark.csv").\
    option("header", "true").\
    save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\BirthbyYear.csv")

# Query 2 - Total number of birth registered in a year by gender

sqlc.sql("Select Year, Gender, sum(Count) from Births group by Gender, Year").show()

BirthbyGender=sqlc.sql("Select Year, Gender, sum(Count) from Births group by Gender, Year")

BirthbyGender.write.\
    format("com.databricks.spark.csv").\
    option("header", "true").\
    save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\BirthbyGender.csv")

# Query 3 - Input a year and populate top 5 most popular names registered that year

sqlc.sql("select Count as NumberOfPeopleWithName, Name from births where Year ="+InYear+" order by count desc limit 5").show()

Mostpopularname=sqlc.sql("select Count as NumberOfPeopleWithName, Name from births where Year = "+InYear+" order by count desc limit 5")

Mostpopularname.write.\
    format("com.databricks.spark.csv").\
    option("header", "true").\
    save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\Mostpopularname.csv")

# Query 4 - Input a name and populate total number of birth registration throughout the dataset for that name

sqlc.sql("select sum(Count) as TotalBirthRegistration from births where Name = '"+InName+"'").show()

TotalbirthRegistration = sqlc.sql("select sum(Count) as TotalBirthRegistration from births where Name = '"+InName+"'")

TotalbirthRegistration.write.\
    format("com.databricks.spark.csv").\
    option("header", "true").\
    save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\TotalbirthRegistration.csv")
    
# Question 4 : NYPD Motor Vehicles Collision dataset 

CollisionSchema = StructType([\
StructField("INCIDENTDATE", StringType(), True),\
StructField("INCIDENTTIME", TimestampType(), True),\
StructField("BOROUGH", StringType(), True),\
StructField("ZIPCODE", StringType(), True),\
StructField("LATITUDE", StringType(), True),\
StructField("LONGITUDE", StringType(), True),\
StructField("LOCATION", StringType(), True),\
StructField("ONSTREETNAME", StringType(), True),\
StructField("CROSSSTREETNAME", StringType(), True),\
StructField("OFFSTREETNAME", StringType(), True),\
StructField("NUMBEROFPERSONSINJURED", IntegerType(), True),\
StructField("NUMBEROFPERSONSKILLED", IntegerType(), True),\
StructField("NUMBEROFPEDESTRIANSINJURED", IntegerType(), True),\
StructField("NUMBEROFPEDESTRIANSKILLED", IntegerType(), True),\
StructField("NUMBEROFCYCLISTINJURED", IntegerType(), True),\
StructField("NUMBEROFCYCLISTKILLED", IntegerType(), True),\
StructField("NUMBEROFMOTORISTINJURED", IntegerType(), True),\
StructField("NUMBEROFMOTORISTKILLED", IntegerType(), True),\
StructField("CONTRIBUTINGFACTORVEHICLE1", StringType(), True),\
StructField("CONTRIBUTINGFACTORVEHICLE2", StringType(), True),\
StructField("CONTRIBUTINGFACTORVEHICLE3", StringType(), True),\
StructField("CONTRIBUTINGFACTORVEHICLE4", StringType(), True),\
StructField("CONTRIBUTINGFACTORVEHICLE5", StringType(), True),\
StructField("UNIQUEKEY", StringType(), True),\
StructField("VEHICLETYPECODE1", StringType(), True),\
StructField("VEHICLETYPECODE2", StringType(), True),\
StructField("VEHICLETYPECODE3", StringType(), True),\
StructField("VEHICLETYPECODE4", StringType(), True),\
StructField("VEHICLETYPECODE5", StringType(), True)])

MotorVehicleCollisions = sqlc.read.format('com.databricks.spark.csv').options(header='true')\
        .load('\\Users\\Yamuna\\Desktop\\Assignment3\\input\\NYPD_Motor_Vehicle_Collisions.csv', schema=CollisionSchema)

# Creating a view on DataFrame for Spark SQL operation

MotorVehicleCollisions.createOrReplaceTempView("Collisions")

# Query 1 -  Capture total injuries and fatalities associated with each motor collision record(identified by a unique incident key)

sqlc.sql("select UNIQUEKEY, (sum(NUMBEROFMOTORISTINJURED) + sum(NUMBEROFMOTORISTKILLED)) \
 as TotalMotoristInjuries\
 from Collisions group by UNIQUEKEY").show()

TotalMotorInjuries = sqlc.sql("select UNIQUEKEY, (sum(NUMBEROFMOTORISTINJURED) + sum(NUMBEROFMOTORISTKILLED)) \
 as TotalMotoristInjuries\
 from Collisions group by UNIQUEKEY")

TotalMotorInjuries.write.\
    format("com.databricks.spark.csv").\
    option("header", "true").\
    save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\TotalMotorInjuries.csv")

#Query 2 - Capture total incident counts in a year (grouped by year)

sqlc.sql("SELECT Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentYear,\
(count(NUMBEROFMOTORISTINJURED) + count(NUMBEROFMOTORISTKILLED)\
+ count(NUMBEROFPERSONSINJURED) + count(NUMBEROFPERSONSKILLED) + count(NUMBEROFPEDESTRIANSINJURED)\
+ count(NUMBEROFCYCLISTINJURED) + count(NUMBEROFCYCLISTKILLED)) as TotalIncidentCounts \
from Collisions \
group by Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd'))").show()

TotalIncidentsYear = sqlc.sql("SELECT Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentYear,\
(count(NUMBEROFMOTORISTINJURED) + count(NUMBEROFMOTORISTKILLED)\
+ count(NUMBEROFPERSONSINJURED) + count(NUMBEROFPERSONSKILLED) + count(NUMBEROFPEDESTRIANSINJURED)\
+ count(NUMBEROFCYCLISTINJURED) + count(NUMBEROFCYCLISTKILLED)) as TotalIncidentCounts \
from Collisions \
group by Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd'))")

TotalIncidentsYear.write.\
    format("com.databricks.spark.csv").\
    option("header", "true").\
    save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\TotalIncidentsYear.csv")

#Query 3 - Capture total injuries(can be sum of injuries and fatalities) grouped by year and quarter

sqlc.sql("SELECT Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentYear,\
Quarter(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentQuarter, \
(sum(NUMBEROFMOTORISTINJURED) + sum(NUMBEROFMOTORISTKILLED)\
+ sum(NUMBEROFPERSONSINJURED) + sum(NUMBEROFPERSONSKILLED) + sum(NUMBEROFPEDESTRIANSINJURED)\
+ sum(NUMBEROFCYCLISTINJURED) + sum(NUMBEROFCYCLISTKILLED)) as SumOfInjuries \
from Collisions \
group by Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')),\
Quarter(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd'))").show()

TotalInjuriesQuarter = sqlc.sql("SELECT Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentYear,\
Quarter(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentQuarter, \
(sum(NUMBEROFMOTORISTINJURED) + sum(NUMBEROFMOTORISTKILLED)\
+ sum(NUMBEROFPERSONSINJURED) + sum(NUMBEROFPERSONSKILLED) + sum(NUMBEROFPEDESTRIANSINJURED)\
+ sum(NUMBEROFCYCLISTINJURED) + sum(NUMBEROFCYCLISTKILLED)) as SumOfInjuries \
from Collisions \
group by Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')),\
Quarter(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd'))")

TotalInjuriesQuarter.write.\
    format("com.databricks.spark.csv").\
    option("header", "true").\
    save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\TotalInjuriesQuarter.csv")

#Query 4 - Capture total injuries(sum of injuries and fatalities) and incident count grouped by Borough, year and month

sqlc.sql("SELECT BOROUGH, Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentYear,\
month(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentMonth, \
(sum(NUMBEROFMOTORISTINJURED) + sum(NUMBEROFMOTORISTKILLED)\
+ sum(NUMBEROFPERSONSINJURED) + sum(NUMBEROFPERSONSKILLED) + sum(NUMBEROFPEDESTRIANSINJURED)\
+ sum(NUMBEROFCYCLISTINJURED) + sum(NUMBEROFCYCLISTKILLED)) as SumOfInjuries \
from Collisions \
group by Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')),\
month(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')), BOROUGH ").show()

TotalInjuriesMYB = sqlc.sql("SELECT BOROUGH, Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentYear,\
month(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')) as IncidentMonth, \
(sum(NUMBEROFMOTORISTINJURED) + sum(NUMBEROFMOTORISTKILLED)\
+ sum(NUMBEROFPERSONSINJURED) + sum(NUMBEROFPERSONSKILLED) + sum(NUMBEROFPEDESTRIANSINJURED)\
+ sum(NUMBEROFCYCLISTINJURED) + sum(NUMBEROFCYCLISTKILLED)) as SumOfInjuries \
from Collisions \
group by Year(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')),\
month(DATE_FORMAT(CAST(UNIX_TIMESTAMP(INCIDENTDATE, 'mm/dd/yyyy') AS TIMESTAMP), 'yyyy-mm-dd')), BOROUGH ")

TotalInjuriesMYB.write.\
    format("com.databricks.spark.csv").\
    option("header", "true").\
    save("\\Users\\Yamuna\\Desktop\\Assignment3\\output\\TotalInjuriesMYB.csv")

