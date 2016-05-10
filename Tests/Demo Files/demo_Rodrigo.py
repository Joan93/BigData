#!/usr/bin/env python

#title           :demo_Rodrigo.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

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


    # sc is an existing SparkContext.
    from pyspark import SparkContext
    from pyspark.sql import SQLContext
    import json
    import datetime
    import os

    sc=SparkContext()
    sqlContext = SQLContext(sc)

    #Generar estadisticas

    path = os.getcwd()+"/Data"
    files = os.listdir(path)

    print " *** END ***"