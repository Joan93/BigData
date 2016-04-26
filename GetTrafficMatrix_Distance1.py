import numpy as np
import math
from collections import OrderedDict
#import resource

#t_ini=time.time()
R = 6371

NumberOfStations=496
Matrix=np.zeros((NumberOfStations,NumberOfStations))

Contador=0
with open("Process_Data/RDD/Prematrix_data_python.txt","r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        partners=f[5]
        p=partners.split(',')
        for element in p:
            #Matrix[int(id)-1,int(element)-1]=1
            #Matrix [int(element)-1,int(id)-1]=1
            dLat = (lat2 - lat1) * (Mathf.PI / 180)
            dLon = (lon2 - lon1) * (Mathf.PI / 180)
            lat1 = lat1 * (Mathf.PI / 180)
            lat2 = lat2 * (Mathf.PI / 180)
            a = math.asin(dLat / 2) * math.asin(dLat / 2) + math.asin(dLon / 2) * math.asin(dLon / 2) * math.acos(
                lat1) * math.acos(lat2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = R * c

np.savetxt('Process_Data/RDD/TrafficMatrix_data_python.txt', Matrix, delimiter=' ',newline='\n',fmt='%i')

