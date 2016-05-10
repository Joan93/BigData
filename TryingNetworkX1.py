import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#El archivo es: TrafficMatrix_data_python
#BaseMap de Matplotlib

NumberOfStations=10
Matrix=np.zeros((NumberOfStations,NumberOfStations))
Status=np.zeros((NumberOfStations,2))

ContadorFilas=0
ContadorColumnas=0
with open("Process_Data/RDD/TrafficMatrix_data_python.txt","r") as fid:
    for line in fid:
        ContadorColumnas=0
        f=line.split(' ')
        for element in f:
            Matrix[ContadorFilas, ContadorColumnas] = element
            if element=="1":
                print "(" + str(ContadorFilas) + "," + str(ContadorColumnas) + ")"
                ContadorColumnas=ContadorColumnas+1
        ContadorFilas=ContadorFilas+1

print Matrix


