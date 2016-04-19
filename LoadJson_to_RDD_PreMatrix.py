#Lucia and Ana work... File 2

import sys
if ("exec" not in sys.argv):
 #Autoexecute SDK
 import os
 os.system('/home/ns3/spark-1.3.0-bin-hadoop2.4/bin/spark-submit LoadJson_to_RDD_PreMatrix.py exec')

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
    time = data.map(lambda line: (line['updateTime']))
    data_filter = data.flatMap(lambda line: line['stations'][:])\
        .map(lambda station: [station['id'],station['streetName'] + " " + station['streetNumber'],station['altitude'],station['latitude'],station['longitude'],station['nearbyStations'],station['type']])

    data_filter.join(time)

    # Falta imprimir en archivo

    import io

    f=io.open("Process_Data/RDD/Prematrix_data_python.txt", 'w+', encoding='utf8')
        #text = f.read()
    #f = open("Process_Data/Ana_data_python.txt", 'w+',encoding='utf8')



    linea= ""
    mostrar = data_filter.collect()
    for a in mostrar:
        for i in range(0,7):
            linea= linea + a[i] + ";"
        f.write(linea+"\n")
        print (linea)
        #f.write("\n")
        print "\n"
        linea=""

