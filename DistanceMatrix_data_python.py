import numpy as np
from collections import OrderedDict
import os
import math

#function to calculate distance
def Cal_distance( lon1,  lat1,   lon2,  lat2):
    R = 6371000# radius of earth in km
    dLat = (lat2-lat1)*(math.pi / 180)
    dLon = (lon2-lon1)*(math.pi / 180)
    lat1 = lat1*(math.pi / 180)
    lat2 = lat2*(math.pi / 180)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

#function to calculate distance
def Cal_Height( height1, height2):
    difference=height1-height2
    return difference


number_stations=465
matrix=np.zeros((number_stations, number_stations))
matrix2=np.zeros((number_stations, number_stations))
neighbours_dic={}
i=0

with open("Process_Data/RDD/Prematrix_data_python.txt", "r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        height=f[2]
        latitude=f[3]
        longitude=f[4]
        partners=f[5]
        all_partners=partners.split(',')
        neighbours_dic[i]=(float(longitude), float(latitude), int(height))
        i+=1
print(neighbours_dic)

#distance matrix
for n in neighbours_dic:
    ne=n+1
    for ne in range(ne,len(neighbours_dic)):
        result = Cal_distance(neighbours_dic.values()[n][0], neighbours_dic.values()[n][1],neighbours_dic.values()[ne][0],neighbours_dic.values()[ne][1])
        matrix[n,ne]=result
        matrix[ne,n]=result
        result2 = Cal_Height(neighbours_dic.values()[n][2],neighbours_dic.values()[ne][2])
        matrix2[n,ne]=result2
        matrix2[ne,n]=result2

np.savetxt('Process_Data/RDD/AlldistanceMatrix_data_python.txt', matrix, delimiter=' ',newline='\n',fmt='%i')
np.savetxt('Process_Data/RDD/AllheightMatrix_data_python.txt', matrix2, delimiter=' ',newline='\n',fmt='%i')

'''
for n in neighbours_tup:
    for ne in neighbours_tup[n][2]:
        n_ne=(int(ne))
        #print(neighbours_tup[n][0]-neighbours_tup[n_ne][0])
        print(n_ne)
        dlat=((neighbours_tup[n][0]-neighbours_tup[n_ne][0])*(pi/180))
        dlon=((neighbours_tup[n][1]-neighbours_tup[n_ne][1])*(pi/180))
        lat=(neighbours_tup[n][0]*(pi/180))
        lon=(neighbours_tup[n][1]*(pi/180))
'''