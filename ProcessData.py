#!/usr/bin/env python

#title           :ProcessData.py
#description     :This script process json files from Barcelona Bicing, filtering and storage in a better form.
#author          :Rodrigo
#date            :2016-04-19
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.6
#requirements    :Spark 1.3
#==============================================================================


# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

spark_path = "/home/rodrigo/Programe_Files_Linux/spark-1.3.0-bin-hadoop2.4/bin/spark-submit"
script_file = "ProcessData.py"
data_folder = "Data/"
data_process_folder = "Process_Data/RDD/"

# Auto-run Pycharm/python to Spark
import sys
import os
if ("exec" not in sys.argv):
 #execute the script vias Spark
 os.system(spark_path+" "+script_file+" exec")

else:
    # **** Script in SPARK ****

    from pyspark import SparkContext
    from pyspark.sql import SQLContext
    import json

    #Config Spark
    sc=SparkContext()
    sqlContext = SQLContext(sc)

    #Load data
    path = data_folder+"data.json"
    data_raw = sc.textFile(path)


    # Parse JSON entries in dataset
    data = data_raw.map(lambda line: json.loads(line))
    # Extract relevant fields in dataset
    time = data.map(lambda line: (line['updateTime']))
    data_filter = data.flatMap(lambda line: line['stations'][:])\
        .map(lambda station: [station['id'],station['altitude'],station['latitude'],station['longitude'],station['bikes'],station['slots'],station['type'],station['status']])
    #Union both dataset
    total =  time.union(data_filter).collect()

    #Write Compact file with filtered data
    f = open(data_process_folder+"data.txt", 'w+')
    line=""
    first= True

    for a in total:
        if(first):
            line= str(a)
            first=False
        else:
         line = str(a[0])+" "+str(a[1])+" "+str(a[2])+" "+str(a[3])+" "+str(a[4])+" "+str(a[5])+" "+str(a[6])+" "+str(a[7])

        #print line
        f.write(line+'\n')

    f.close()