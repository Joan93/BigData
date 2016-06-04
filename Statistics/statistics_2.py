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
    from pyspark import SparkContext
    from operator import add
    from pyspark.sql import SQLContext
    import numpy as np
    from pyspark.sql import *
    from pyspark.mllib.linalg import Vectors
    import re

    sc=SparkContext()

    vn = np.array([21, 10, 2, 2, 7])
    v0 = Vectors.dense(vn)
    v1 = Vectors.dense([22, 10, 2, 3, 7])
    v2 = Vectors.dense([23, 10, 2, 3, 7])

    rows = sc.parallelize([v0, v1, v2])

    summary = Statistics.colStats(rows)


    print ("Datos estadistica")
    # estadisticas
    print("media:"),(summary.mean())
    print("varianza:"),(summary.variance())
    print("non Zeros:"),(summary.numNonzeros())
    print ("max:"),(summary.max())
    print ("min:"),(summary.min())
