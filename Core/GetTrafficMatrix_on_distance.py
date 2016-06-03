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


def run_main():

    NumberOfStations=465
    Matrix=np.zeros((NumberOfStations,NumberOfStations))

    InputFile = conf.data_process_file_distancematrix
    OutputFile= conf.data_process_file_adjacentmatrix_distance
    distance_neigbours = 500
    min_neigbours=4

    Distance_matrix = np.loadtxt(InputFile,delimiter=' ',dtype=np.dtype('int32'))

    nummax_enlaces=0
    factor=1

    total_enlaces=0
    i=0
    while(i<NumberOfStations-1):
        num_enlaces=0
        distance_range=factor*distance_neigbours
        print "range: "+str(distance_range)

        for j in range (0,NumberOfStations):
            print Distance_matrix[i,j]
            if(Distance_matrix[i,j]<(distance_range+1)):
                num_enlaces+=1
                Matrix[i,j]=1
                Matrix [j,i]=1

        if(num_enlaces<(min_neigbours+1) and num_enlaces>=(NumberOfStations-i)):
            factor=factor*2
            print "["+str(i)+","+str(j)+"] : factor "+str(factor)
        else:
            print "["+str(i)+","+str(j)+"] : enlaces "+str(num_enlaces)
            if(num_enlaces>nummax_enlaces):
                nummax_enlaces=num_enlaces
            factor=1
            total_enlaces+=num_enlaces
            i+=1


    print ("Numero enlacesmax: "+str(nummax_enlaces))
    print ("Numero total: "+str(total_enlaces))
    print ("Numero medio enlaces: "+str(total_enlaces/NumberOfStations))

    #
    # print("Numero medio de enlaces: "+str(float(media/NumberOfStations)))
    # print("Numero max de enlaces: "+str(nummax_enlaces))
    # print("Numero min de enlaces: "+str(nummin_enlaces))


    np.savetxt(OutputFile, Matrix, delimiter=' ',newline='\n',fmt='%i')