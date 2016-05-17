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
 os.system('/home/lucia/spark-1.3.0-bin-hadoop2.4/bin/spark-submit statistics.py exec')

# Programa
else:
    from pyspark.mllib.stat import Statistics
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
    file=sc.textFile("Process_Data/RDD/SuperFile/superfile.dat")
    row = file.map(lambda line:line.split(' ')[1:len(line)]).filter(lambda x: x.startswith(' '),file) #http://www.u.arizona.edu/~erdmann/mse350/topics/list_comprehensions.html
    row_lst=row.collect() #converts rdd to list
    print(row_lst)
    ln=[]
    v=[]
    for l in row_lst:
        for sl in l:
            ln.append(int(sl))
        vt=Vectors.dense(ln)
        v.append(vt)
    #v=Vectors.dense(row_lst)
    listings=sc.parallelize(v)
    summary = Statistics.colStats(listings)

    print("media:"),(summary.mean())
    print("varianza:"),(summary.variance())
    print ("max:"),(summary.max())
    print ("min:"),(summary.min())
    print("non Zeros:"),(summary.numNonzeros())


