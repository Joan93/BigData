#!/usr/bin/env python

#title           :LoadJson_to_RDD.py
#description     :This script process the data in json format to compact interesting data files.
#author          :Rodrigo
#date            :2016-04-10
#version         :0.2
#usage           :python LoadJson_to_RDD.py
#notes           :
#python_version  :2.7.6
#requirements    :Spark 1.6

#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================

import config as conf

spark_path = conf.spark_path
script_file = "LoadJson_to_RDD.py"
data_folder = conf.data_folder
data_process_folder = conf.data_process_historical
command_execution = spark_path+" "+conf.core_folder+script_file+" exec"

def run_main(alone):
    os.system(command_execution)

# Auto-run Pycharm/python to Spark
import sys
import os
if ("exec" not in sys.argv):
 #execute the script vias Spark
 #os.system(spark_path+" "+script_file+" " exec)
 if(conf.verbose):
     print "Load RDD process Json"

else:
    # **** Script in SPARK ****


    from pyspark import SparkContext
    from pyspark.sql import SQLContext
    import json
    import datetime
    import os

    sc=SparkContext()
    sqlContext = SQLContext(sc)

    #path = os.getcwd()+"/Data"
    files = os.listdir(data_folder)
    total_files = len(files)
    i=0
    for file in files:

        data_raw = sc.textFile(data_folder+file)
        #print data_raw

        # Parse JSON entries in dataset
        data = data_raw.map(lambda line: json.loads(line))

        # Extract relevant fields in dataset -- category label and text content
        time = data.map(lambda line: (line['updateTime']))
        #data_filter = data.flatMap(lambda line: line['stations'][:])\
        #    .map(lambda station: [station['id'],station['altitude'],station['latitude'],station['longitude'],station['bikes'],station['slots'],station['type'],station['status']])
        data_filter = data.flatMap(lambda line: line['stations'][:])\
            .map(lambda station: [station['id'],station['bikes'],station['status']])

        #total = time.union(data_filter).collect()

        time = time.collect()
        #GEN FILENAME
        line=""
        hora=datetime.datetime.fromtimestamp(time[0]).strftime('%H')
        min=datetime.datetime.fromtimestamp(time[0]).strftime('%M')
        dia = datetime.datetime.fromtimestamp(time[0]).weekday()
        horasmin=(int(min)+int(int(hora)*60))/3
        totaltime=dia*1000+horasmin
        line= str(time[0])+"_"+str(totaltime).zfill(4)
        #for data[""]

        filename = file.split(".")
        f = open(data_process_folder+line+".txt", 'w+')

        line=""
        for a in data_filter.collect():
            #line = str(a[0])+" "+str(a[1])+" "+str(a[2])+" "+str(a[3])+" "+str(a[4])+" "+str(a[5])+" "+str(a[6])+" "+str(a[7])
            line = str(a[0])+" "+str(a[1])+" "+str(a[2])
            #print line
            f.write(line+'\n')
        i+=1

        if(conf.verbose):
            porcentaje = float(i*100/total_files)
            line_porc="|"
            for m in range(0,int(porcentaje)):
                line_porc+="="
            print line_porc.rstrip('\n')+"| "+str(porcentaje)+"% \n \n \n"
            print("Procesando ... ")
        f.close()