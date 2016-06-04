#!/usr/bin/env python

#title           :statistics.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

import sys
import numpy as np
if ("exec" not in sys.argv):
 #Autoexecute SDK
 import os
 import re
 os.system('/home/lucia/spark-1.3.0-bin-hadoop2.4/bin/spark-submit Statistics/statistics.py exec')
 #os.system('/home/lucia/spark-1.3.0-bin-hadoop2.4/python/pyspark/mllib/stat statistics.py exec')
# Programa
else:
    from pyspark.mllib.stat import Statistics
    from decimal import Decimal as D
    from pyspark import SparkContext
    from operator import add
    from pyspark.sql import SQLContext
    import numpy as np
    from pyspark.sql import *
    from pyspark.mllib.linalg import Vectors
    import re

    sc=SparkContext()
    '''
    vn = np.array([1.0, 9.0, 9.0])
    v0 = Vectors.dense(vn)
    v1 = Vectors.dense([2.0, 3.0, 4.0])
    v2 = Vectors.dense([3.0, 3.0, 4.0])

    rows = sc.parallelize([v0, v1, v2])

    summary = Statistics.colStats(rows)


    print ("Datos estadistica")
    # estadisticas
    print("media:"),(summary.mean())
    print("varianza:"),(summary.variance())
    print("non Zeros:"),(summary.numNonzeros())
    print ("max:"),(summary.max())
    print ("min:"),(summary.min())


    # correlacion
    print (" ")
    print (" ")
    print ("matriz de correlacion:")
    print (" ")
    print(Statistics.corr(rows, method="pearson"))

    # carreguem fitxer

    '''

    file=sc.textFile("Process_Data/SuperFile/superfile.dat")
    row = file.map(lambda line:line.split(' ')[1:len(line)]).map(lambda xs: [float(x) for x in xs])
    row_list= row.collect() #transforms to list
    print(row_list)
    print(row_list[0])

    for i in range(0,len(row_list)):
        v=Vectors.dense(row_list[i])
        rows = sc.parallelize([v])
        i+=1

    summary = Statistics.colStats(rows)

    print("media:"),(summary.mean())
    print("varianza:"),(summary.variance())
    print ("max:"),(summary.max())
    print ("min:"),(summary.min())
    print("non Zeros:"),(summary.numNonzeros())