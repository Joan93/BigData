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

 sc=SparkContext()

 file=sc.textFile("traffic1hour.exp2")


 dep=file.map(lambda line: line.split(";")[0])\
	.map(lambda word: (word, 1))\
	.reduceByKey(add)

 print dep
 print(dep.mean())


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