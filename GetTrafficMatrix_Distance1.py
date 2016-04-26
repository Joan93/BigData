import numpy as np
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
            a = Mathf.Sin(dLat / 2) * Mathf.Sin(dLat / 2) + Mathf.Sin(dLon / 2) * Mathf.Sin(dLon / 2) * Mathf.Cos(
                lat1) * Mathf.Cos(lat2);
            c = 2 * Mathf.Atan2(Mathf.Sqrt(a), Mathf.Sqrt(1 - a));
            d = R * c;

np.savetxt('Process_Data/RDD/TrafficMatrix_data_python.txt', Matrix, delimiter=' ',newline='\n',fmt='%i')

