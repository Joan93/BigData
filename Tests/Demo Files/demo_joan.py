#!/usr/bin/env python

#title           :demo_Joan.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group formed by Ana, Lucia, Joan and Rodrigo


# PARA EJECUTAR EL PROGRAMA en pycharm con pyspark



float CalcDistance(float lon1, float lat1, float lon2, float lat2){
		int R = 6371; // radius of earth in km
		float dLat = (lat2-lat1)*(Mathf.PI / 180);
		float dLon = (lon2-lon1)*(Mathf.PI / 180);
		lat1 = lat1*(Mathf.PI / 180);
		lat2 = lat2*(Mathf.PI / 180);
		float a = Mathf.Sin(dLat/2) * Mathf.Sin(dLat/2) + Mathf.Sin(dLon/2) * Mathf.Sin(dLon/2) * Mathf.Cos(lat1) * Mathf.Cos(lat2);
		float c = 2 * Mathf.Atan2(Mathf.Sqrt(a), Mathf.Sqrt(1-a));
		float d = R * c;
		return d; //distance in kms
	}




'''







import sys
if ("exec" not in sys.argv):
 #Autoexecute SDK
 import os
 os.system('/Users/JoanIgnasi/Documents/spark-1.3.0-bin-hadoop2.4/bin/spark-submit demo_joan.py exec')


#Programa

else:
 from pyspark.mllib.stat import Statistics

#ejemplo de media, etc...

 sc = ... # SparkContext

 mat = ... # an RDD of Vectors

 # Compute column summary statistics.
 summary = Statistics.colStats(mat)
 print summary.mean()
 print summary.variance()
 print summary.numNonzeros()


#correlacion entre series

 from pyspark.mllib.stat import Statistics

 sc = ... # SparkContext

 seriesX = ... # a series
 seriesY = ... # must have the same number of partitions and cardinality as seriesX

 # Compute the correlation using Pearson's method. Enter "spearman" for Spearman's method. If a
 # method is not specified, Pearson's method will be used by default.
 print Statistics.corr(seriesX, seriesY, method="pearson")

 data = ... # an RDD of Vectors
 # calculate the correlation matrix using Pearson's method. Use "spearman" for Spearman's method.
 # If a method is not specified, Pearson's method will be used by default.
 print Statistics.corr(data, method="pearson")




   # sc is an existing SparkContext.
    from pyspark import SparkContext
    from pyspark.sql import SQLContext

    sc=SparkContext()
    sqlContext = SQLContext(sc)

    # A JSON dataset is pointed to by path.
    # The path can be either a single text file or a directory storing text files.
    path = "Data/data.json"

    # Create a SchemaRDD from the file(s) pointed to by path
    data = sqlContext.jsonFile(path)

    # The inferred schema can be visualized using the printSchema() method.
    data.printSchema()
    # root
    # |-- stations: array (nullable = true)
    # |    |-- element: struct (containsNull = true)
    # |    |    |-- altitude: string (nullable = true)
    # |    |    |-- bikes: string (nullable = true)
    # |    |    |-- id: string (nullable = true)
    # |    |    |-- latitude: string (nullable = true)
    # |    |    |-- longitude: string (nullable = true)
    # |    |    |-- nearbyStations: string (nullable = true)
    # |    |    |-- slots: string (nullable = true)
    # |    |    |-- status: string (nullable = true)
    # |    |    |-- streetName: string (nullable = true)
    # |    |    |-- streetNumber: string (nullable = true)
    # |    |    |-- type: string (nullable = true)
    # |-- updateTime: long (nullable = true)


    data.registerTempTable("data")

    # SQL statements can be run by using the sql methods provided by `sqlContext`.
    filterdata = sqlContext.sql("SELECT stations.id, stations.latitude, stations.longitude, stations.bikes,"
                                " stations.slots, stations.status, stations.type updateTime FROM data ORDER BY stations.id ")


    '''
    # Register this SchemaRDD as a table.
    data.registerTempTable("data")

    # SQL statements can be run by using the sql methods provided by sqlContext.
    teenagers = sqlContext.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")
    '''

    # Alternatively, a SchemaRDD can be created for a JSON dataset represented by
    # an RDD[String] storing one JSON object per string.
    anotherPeopleRDD = sc.parallelize([
      '{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}'])
    anotherPeople = sqlContext.jsonRDD(anotherPeopleRDD)
    '''


''''
# sc is an existing SparkContext.
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

# A JSON dataset is pointed to by path.
# The path can be either a single text file or a directory storing text files.
path = "examples/src/main/resources/people.json"
# Create a SchemaRDD from the file(s) pointed to by path
people = sqlContext.jsonFile(path)

# The inferred schema can be visualized using the printSchema() method.
people.printSchema()
# root
#  |-- age: IntegerType
#  |-- name: StringType

# Register this SchemaRDD as a table.
people.registerTempTable("people")

# SQL statements can be run by using the sql methods provided by sqlContext.
teenagers = sqlContext.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# Alternatively, a SchemaRDD can be created for a JSON dataset represented by
# an RDD[String] storing one JSON object per string.
anotherPeopleRDD = sc.parallelize([
  '{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}'])
anotherPeople = sqlContext.jsonRDD(anotherPeopleRDD)


'''