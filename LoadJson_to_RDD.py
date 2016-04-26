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
    import datetime
    import os

    sc=SparkContext()
    sqlContext = SQLContext(sc)

    path = os.getcwd()+"/Data"
    files = os.listdir(path)
    for file in files:

        data_raw = sc.textFile(path+"/"+file)
        #print data_raw

        # Parse JSON entries in dataset
        data = data_raw.map(lambda line: json.loads(line))

        # Extract relevant fields in dataset -- category label and text content
        time = data.map(lambda line: (line['updateTime']))
        data_filter = data.flatMap(lambda line: line['stations'][:])\
            .map(lambda station: [station['id'],station['altitude'],station['latitude'],station['longitude'],station['bikes'],station['slots'],station['type'],station['status']])

        total = time.union(data_filter).collect()

        #for data[""]
        filename = file.split(".")
        f = open(os.getcwd()+"/Process_Data/RDD/"+filename[0]+".txt", 'w+')

        line=""
        first= True

        for a in total:
            if(first):
                time=a
                hora=datetime.datetime.fromtimestamp(time).strftime('%H')
                min=datetime.datetime.fromtimestamp(time).strftime('%M')
                dia = datetime.datetime.fromtimestamp(time).weekday()

                horasmin=(int(min)+int(int(hora)*60))/3

                totaltime=dia*1000+horasmin

                line= str(a)+" "+str(totaltime)
                first=False
            else:
             line = str(a[0])+" "+str(a[1])+" "+str(a[2])+" "+str(a[3])+" "+str(a[4])+" "+str(a[5])+" "+str(a[6])+" "+str(a[7])

            #print line
            f.write(line+'\n')

        f.close()