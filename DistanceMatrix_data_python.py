import numpy as np
from collections import OrderedDict
import os

number_stations=496
pi=3.14159265358979323846
radius=6371 #radius of earth in km

matrix=np.zeros((number_stations, number_stations))
altitude_arr=([])
longitude_arr=([])
latitude_arr=([])
neighbours_tup={}
i=0
n=0
with open("Process_Data/RDD/Prematrix_data_python.txt", "r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        altitude=f[2]
        latitude=f[3]
        longitude=f[4]
        partners=f[5]
        all_partners=partners.split(',')
        neighbours_tup[i]=(float(latitude), float(longitude), all_partners)
        i+=1

print(neighbours_tup)

for n in neighbours_tup:
    for ne in neighbours_tup[n][2]:
        n_ne=(int(ne))
        print(neighbours_tup[n][0]-neighbours_tup[n_ne][0])






        #altitude_arr=np.append(altitude_arr, altitude)
        #latitude_arr=np.append(latitude_arr, latitude)
        #longitude_arr=np.append(longitude_arr, longitude)



'''for i in stations:
    latitude()



        for element in all_partners:
            matrix[int(id)-1,int(element)-1]=
            matrix[int(element)-1,int(id)-1]=1
        '''