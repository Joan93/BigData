import numpy as np
from collections import OrderedDict
import os

stations=np.array([])
number_stations=496
matrix=np.zeros((number_stations, number_stations))
altitude=np.array([])
with open("Process_Data/RDD/Prematrix_data_python.txt", "r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        address=f[1]
        height=f[2]
        partners=f[5]
        all_partners=partners.split(',')
        stations=np.append(stations, id)
        altitude=np.append(altitude, height)
        for element in all_partners:
            matrix[int(id)-1,int(element)-1]=1
            matrix[int(element)-1,int(id)-1]=1
print(altitude)
np.savetxt('Process_Data/RDD/TrafficMatrix_data_python.txt', matrix, delimiter=' ',newline='\n',fmt='%i')#

print(np.argmin(altitude)) #minimum altitude: 11m
print(np.argmax(altitude)) #maximum altitude: 331m
