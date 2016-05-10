#!/usr/bin/env python

#title           :statistics.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

import sys
if ("exec" not in sys.argv):
 #Autoexecute SDK
 import os
 os.system('/Users/JoanIgnasi/Documents/spark-1.3.0-bin-hadoop2.4/bin/spark-submit statistics.py exec')


# Programa
else:

 from pyspark.mllib.stat import Statistics
 from pyspark import SparkContext
 from operator import add
 from pyspark.sql import SQLContext
 import numpy as np
 from pyspark.sql import *
 from pyspark.mllib.linalg import Vectors

 sc=SparkContext()

 vn=np.array([1.0, 9.0, 9.0])

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

 file="Process_Data/RDD/SuperFile/superfile.dat"

 airports=np.array([])
 with open(file,"r")as fid:
    for line in fid:
        f=line.split(' ')
        dep=f[1]
        print dep
        '''
        arr=f[2]
        airports=np.array(dep)
 print (airports)

 v0 = Vectors.dense(airports)
 print v0



    dim=len(airports)
    xtrafil=np.zeros((dim,dim))

 with open(file,"r")as fid:
    for line in fid:
        f=line.split(' ')
        dep=f[0]
        arr=f[1]
        fil=np.where(airports==dep)
        column=np.where(airports==arr)
        xtrafil[fil,column]=xtrafil[fil,column]+1
    sd=xtrafil.sum(axis=0)
    sa=xtrafil.sum(axis=1)
    st=sd+sa
 d = zip(airports, st, sd, sa)

 print d
 '''