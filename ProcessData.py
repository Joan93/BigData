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
data_folder = "Process_Data/RDD/"
data_process_folder = "Process_Data/RDD/SuperFile"

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
    # Define the Header of RDD
    # idlabel timestamp1, timestamp2 , tamstampn....


    for file in files:

        path = data_folder+file
        #Get th timestamp and pseudotime
        time = path[:-3].split('_')
        pseudotime = int(time[1])
        timestamp= int(time[0])

        data_raw = sc.textFile(path)




    f = open(data_process_folder+file, 'w+')
    line=""
    first= True
    #WRite the super File
    for a in total:
            if(first):
                line= str(a)
                first=False
            else:
             line = str(a[0])+" "+str(a[1])+" "+str(a[2])+" "+str(a[3])+" "+str(a[4])+" "+str(a[5])+" "+str(a[6])+" "+str(a[7])

            #print line
            f.write(line+'\n')

        f.close()