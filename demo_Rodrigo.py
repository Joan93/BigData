#!/usr/bin/env python

#title           :demo_Rodrigo.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

spark_path = "/home/rodrigo/Programe_Files_Linux/spark-1.3.0-bin-hadoop2.4/bin/spark-submit"
script_file = "demo_Rodrigo.py"
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
    files = os.listdir(data_folder)

    path = data_folder+"03-17_2016_13_24.json"
    #path = data_folder+"data2.json"
    data_raw = sc.textFile(path)
    print path
    # Parse JSON entries in dataset
    data = data_raw.map(lambda line: json.loads(line))
    print data_raw
    print data

    # Extract relevant fields in dataset
    time = data.map(lambda line: (line['updateTime']))


    data_filter = data.flatMap(lambda line: line['stations'][:])\
        .map(lambda station: [station['id'],station['altitude'],station['latitude'],station['longitude'],station['bikes'],station['slots'],station['type'],station['status']])

    print time.first()
    print data_filter.first()

    #Union both dataset
    total =  time.union(data_filter).collect()

    #Write Compact file with filtered data
    f = open(data_process_folder+"data5.txt", 'w+')
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

    print " *** END ***"