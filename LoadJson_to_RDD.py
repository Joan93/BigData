#Rodrigo Demo file to work alone

import sys
if ("exec" not in sys.argv):
 #Autoexecute SDK
 import os
 os.system('/home/rodrigo/Programe_Files_Linux/spark-1.3.0-bin-hadoop2.4/bin/spark-submit LoadJson_to_RDD.py exec')

else:

    # sc is an existing SparkContext.
    from pyspark import SparkContext
    from pyspark.sql import SQLContext
    import json

    sc=SparkContext()
    sqlContext = SQLContext(sc)

    path = "Data/data.json"

    data_raw = sc.textFile(path)
    # Parse JSON entries in dataset
    data = data_raw.map(lambda line: json.loads(line))

    # Extract relevant fields in dataset -- category label and text content
    time = data.map(lambda line: (line['updateTime'])).first()
    data_pared = data.flatMap(lambda line: line['stations'][:]).map(lambda station: [station['id'],station['altitude'],station['longitude']])

    mostrar = data_pared.collect()
    for a in mostrar:
        print a
