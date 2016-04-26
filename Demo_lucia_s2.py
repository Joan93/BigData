import numpy as np
import os

stations=np.array([])


with open("Process_Data/RDD/Prematrix_data_python.txt", "r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        address=f[1]
        partners=f[5]
        all_partners=partners.split(',')
        stations=np.append(stations, id)
        #print(all_partners)

matrix=np.zeros((len(stations), len(stations)))
#print(matrix)

with open("Process_Data/RDD/Prematrix_data_python.txt", "r") as fid:
    for line in fid:
        f=line.split(';')
        position_row= np.where(stations==all_partners)
        position_col= np.where(airports==arr)
        matrix[position_row, position_col]= matrix[position_row, position_col]+1
