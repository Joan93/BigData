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


 v0 = Vectors.dense([1.0, 9.0, 9.0])
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

