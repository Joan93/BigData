import sys
if ("exec" not in sys.argv):
 #Autoexecute SDK
 import os
 os.system('/home/lucia/spark-1.3.0-bin-hadoop2.4/bin/spark-submit teststat.py exec')

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

    line ='1458147489;2359 8 6 2 2 9 11 11 9 10 7 0 0 0 6 10 0 0 1 12 0 0 24 12 10 8 9 1 2 6 13 0 15 1 13'
    line = line.translate(None, ';')
    print(clean_line)
    results = [int(i) for i in clean_line]
    values=map(int,results)
    bikes=clean_line.pop(0)
    print(bikes)


    '''bikes_st=f[ColNum]
    bikes=np.array(bikes_st)
    bike_vec=Vectors.dense(bikes)
    #parallelize

    print(bikes)
        '''