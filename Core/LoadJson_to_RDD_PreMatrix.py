#!/usr/bin/env python

#title           :LoadJson_to_RDD_PreMatrix.py
#description     :This script process the data in json format to compact teh static data in one file.
#author          :Lucia & Ana
#date            :2016-04-20
#version         :0.3
#usage           :python LoadJson_to_RDD.py
#notes           :
#python_version  :2.7.6
#requirements    :Spark 1.6

#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================

import sys
import config as conf
import os

spark_path = conf.spark_path
script_file = "LoadJson_to_RDD_PreMatrix.py"
data_folder = conf.data_folder
data_process_file_prematrix = conf.data_process_file_prematrix_error
command_execution = spark_path+" "+conf.core_folder+script_file+" exec"

def run_main():
    os.system(command_execution)

if ("exec" not in sys.argv):
 #Autoexecute SDK
 os.system(command_execution)
 #os.system('/home/ns3/spark-1.3.0-bin-hadoop2.4/bin/spark-submit LoadJson_to_RDD_PreMatrix.py exec')

else:

    # sc is an existing SparkContext.
    from pyspark import SparkContext
    from pyspark.sql import SQLContext
    import json


    sc=SparkContext()
    sqlContext = SQLContext(sc)

    #path = "Data/data.json"
    path = data_folder
    files = os.listdir(path)
    print files[0]
    data_raw = sc.textFile(path+"/"+files[0])
    # Parse JSON entries in dataset
    data = data_raw.map(lambda line: json.loads(line))

    # Extract relevant fields in dataset -- category label and text content
    time = data.map(lambda line: (line['updateTime']))
    data_filter = data.flatMap(lambda line: line['stations'][:])\
        .map(lambda station: [station['id'],station['streetName'] + " " + station['streetNumber'],station['altitude'],station['latitude'],station['longitude'],station['nearbyStations'],station['type'],station['status']])

    data_filter.join(time)

    # Falta imprimir en archivo

    import io

    f=io.open(data_process_file_prematrix, 'w+', encoding='utf8')
        #text = f.read()
    #f = open("Process_Data/Ana_data_python.txt", 'w+',encoding='utf8')


    linea= ""
    mostrar = data_filter.collect()
    for a in mostrar:
        for i in range(0,8):
            linea= linea + a[i] + ";"
        f.write(linea+"\n")
        #print (linea)
        #f.write("\n")
        #print "\n"
        linea=""

