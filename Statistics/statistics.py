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
    # correlacion
    print (" ")
    print (" ")
    print ("matriz de correlacion:")
    print (" ")
    print(Statistics.corr(rows, method="pearson")

    '''

    file=sc.textFile("Process_Data/SuperFile/superfile.dat")

    row = file.map(lambda line:line.split(' ')[1:len(line)]).map(lambda xs: [float(x) for x in xs])
    row_list= row.collect() #transforms to list
    print(row_list)

    #matrix
    w, h = 1,38
    new_list = [[0 for x in range(w)] for y in range(h)]

    for i in range(0,len(row_list)):
        new_list[i][:]=Vectors.dense(row_list[i])
        i+=1
    rows = sc.parallelize([new_list])
    print(rows)
    summary = Statistics.colStats(rows)


    print("media:"),(summary.mean())
    print("varianza:"),(summary.variance())
    print ("max:"),(summary.max())
    print ("min:"),(summary.min())
    print("non Zeros:"),(summary.numNonzeros())