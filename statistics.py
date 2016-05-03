#!/usr/bin/env python

#title           :demo_Rodrigo.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo



import sys
if ("exec" not in sys.argv):
 #Autoexecute SDK
 import os
 os.system('/Users/JoanIgnasi/Documents/spark-1.6.1-bin-hadoop2.6/bin/spark-submit statistics.py exec')


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
 print(summary.mean())
 print(summary.variance())
 print(summary.numNonzeros())
 print (summary.max())
 print (summary.min())


 '''

 rdd = sc.parallelize([range(0, 10), range(10,20), range(20, 30)])


 #mat = ([2, 0, 0, -2])

# print rdd.mean()
 xs = (("x1", 1), ("x2", 2), ("x3", 3))
 datos=zip(*xs)
 #datos = np.array([7,8,1,3])
 mat = sc.parallelize(datos)



 #summary = Statistics.colStats(rdd)

 print(dep.mean())
 print(summary.variance())
 print(summary.numNonzeros())
  '''