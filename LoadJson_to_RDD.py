#!/usr/bin/env python

#title           :demo_Rodrigo.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

#spark_path = "/home/rodrigo/Programe_Files_Linux/spark-1.3.0-bin-hadoop2.4/bin/spark-submit"
spark_path = "/home/rodrigo/Programe_Files_Linux/spark-1.6.1-bin-hadoop2.6/bin/spark-submit"
script_file = "LoadJson_to_RDD.py"
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
    import datetime
    import os

    sc=SparkContext()
    sqlContext = SQLContext(sc)

    #path = os.getcwd()+"/Data"
    files = os.listdir(data_folder)
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
            .map(lambda station: [station['id'],station['bikes']])

        #total = time.union(data_filter).collect()

        time = time.collect()
        #GEN FILENAME
        line=""
        hora=datetime.datetime.fromtimestamp(time[0]).strftime('%H')
        min=datetime.datetime.fromtimestamp(time[0]).strftime('%M')
        dia = datetime.datetime.fromtimestamp(time[0]).weekday()
        horasmin=(int(min)+int(int(hora)*60))/3
        totaltime=dia*1000+horasmin
        line= str(time[0])+"_"+str(totaltime)
        #for data[""]

        filename = file.split(".")
        f = open(data_process_folder+line+".txt", 'w+')


        line=""
        for a in data_filter.collect():
            #line = str(a[0])+" "+str(a[1])+" "+str(a[2])+" "+str(a[3])+" "+str(a[4])+" "+str(a[5])+" "+str(a[6])+" "+str(a[7])
            line = str(a[0])+" "+str(a[1])
            #print line
            f.write(line+'\n')

        f.close()