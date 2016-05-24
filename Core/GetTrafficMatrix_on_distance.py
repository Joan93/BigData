#!/usr/bin/env python

#title           :GetTrafficMatrix_ondistance.py
#description     :This script process PReMatrix file to get Adjacent matrix of netwok.
#author          :Lucia
#date            :2016-04-28
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.6
#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================

###################################################################################
#                                                                                 #
#  Obtener la matrix de conectividad en funcion de la distancia entre estaciones  #
#                                                                                 #
###################################################################################

import numpy as np
import config as conf


NumberOfStations=465
Matrix=np.zeros((NumberOfStations,NumberOfStations))
Status=np.zeros((NumberOfStations,2))
InputFile = conf.data_process_file_prematrix
OutputFile= conf.data_process_file_adjacentmatrix

Distance_matrix = np.loadtxt('Process_Data/RDD/AlldistanceMatrix_data_python.txt',delimiter=' ',dtype=np.dtype('int32'))

contador=0
nummax_enlaces =0
nummin_enlaces=0
media=0
with open("Process_Data/Prematrix_data_python_fix.txt","r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        partners=f[5]
        status=f[7]
        Status[contador - 1, 0]=id
        if status=="OPN":
            Status[contador-1,1]=1
        else:
            Status[contador-1,1]=0

        num_enlaces = 0
        for x in range(contador+1, NumberOfStations-1):

            if(Distance_matrix[contador,x]<1001):
                num_enlaces+=1
                Matrix[contador,x]=1
                Matrix [x,contador]=1


        print ("Numero enlaces: "+str(num_enlaces))
        if(num_enlaces>nummax_enlaces):
            nummax_enlaces=num_enlaces

        if(num_enlaces<nummin_enlaces):
            nummin_enlaces=num_enlaces

        media +=num_enlaces
        contador+=1
        #    print element
        #print "\n \n"

print("Numero medio de enlaces: "+str(float(media/NumberOfStations)))
print("Numero max de enlaces: "+str(nummax_enlaces))
print("Numero min de enlaces: "+str(nummin_enlaces))

#elimino aquellas estaciones que no estan disponibles
index=0
for element in Status[:,1]:
    if element == 0:
        Matrix[:,index]=0
        Matrix[index,:]=0
    index = index + 1


np.savetxt('Process_Data/RDD/TrafficMatrix_data_3km.txt', Matrix, delimiter=' ',newline='\n',fmt='%i')