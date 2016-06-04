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

#sudo pip install matplotlib

import numpy as np
import config as conf
import networkx as nx
import matplotlib
import math



def run_main(num):


    if(num==1000):
        adj = np.loadtxt(conf.data_process_file_adjacentmatrix_distance_1000,delimiter=' ',dtype=np.dtype('int32'))
        OutputFile = conf.data_process_file_weight_edgematrix_1000
    elif(num==300):
        adj = np.loadtxt(conf.data_process_file_adjacentmatrix_distance_300,delimiter=' ',dtype=np.dtype('int32'))
        OutputFile = conf.data_process_file_weight_edgematrix_300
    elif(num==-1):
        adj = np.loadtxt(conf.data_process_file_adjacentmatrix,delimiter=' ',dtype=np.dtype('int32'))
        OutputFile = conf.data_process_file_weight_edgematrix_distance
    else:
        adj = np.loadtxt(conf.data_process_file_adjacentmatrix_distance,delimiter=' ',dtype=np.dtype('int32'))
        OutputFile = conf.data_process_file_weight_edgematrix_ref

    distances = np.loadtxt(conf.data_process_file_distancematrix,delimiter=' ',dtype=np.dtype('int32'))
    inclinacion = np.loadtxt(conf.data_process_file_inclination_matrix,delimiter=' ',dtype=np.dtype('int32'))

    weight_matrix=np.zeros((distances.shape[0], distances.shape[1]))

    for i in range(0,distances.shape[0]):
     for j in range(i,distances.shape[0]):

        if(adj[i,j]==1):
            distance = distances[i,j]
            slope = inclinacion[i,j]

            if(slope>0):
                y=60
            else:
                y=15

            if(distance<2000):
                weight=(float(distance/1000.0)*(1+y*slope))*100.0
            elif(distance<6000):
                weight=(2 +float((distance-2000.0)/500.0)*(1+y*slope))*100.0
            elif(distance<6000):
                weight=(10 +12*math.exp(float(distance/6000.0))*(1+y*slope))*100.0
            else:
                weight=9999

        else:
            weight=9999

        weight_matrix[i,j]=weight
        weight_matrix[j,i]=weight

    np.savetxt(OutputFile, weight_matrix, delimiter=' ',newline='\n',fmt='%i')