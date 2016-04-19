#Rodrigo Demo file to work alone

import sys
if ("exec" not in sys.argv):
 #Autoexecute SDK
 import os
 os.system('/home/rodrigo/Programe_Files_Linux/spark-1.3.0-bin-hadoop2.4/bin/spark-submit demo_Rodrigo.py exec')

else:

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
