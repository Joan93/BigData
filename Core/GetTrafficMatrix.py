#!/usr/bin/env python

#title           :GetTrafficMatrix.py
#description     :This script process PReMatrix file to get Adjacent matrix of netwok.
#author          :Ana Cristina
#date            :2016-04-25
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
#   Obtener la matrix de conectividad en funcion del estado de las estaciones     #
#                                                                                 #
###################################################################################

def run_main():

    import numpy as np
    from collections import OrderedDict
    import config as conf
    import IdDictionary

    InputFile = conf.data_process_file_prematrix
    OutputFile= conf.data_process_file_adjacentmatrix

    NumberOfStations=465
    #create matrix with zeros
    Matrix=np.zeros((NumberOfStations,NumberOfStations))
    Status=np.zeros((NumberOfStations,2))

    #import diccionary for id and position
    superdict = IdDictionary.run_main()

    contador=-1
    with open(InputFile,"r") as fid:
        for line in fid:
            f=line.split(';')
            id=f[0]
            partners=f[5]
            status=f[7]
            p=partners.split(',')
            Status[contador, 0]=id
            Status[contador,1]=1

            for element in p:
                posicion = int((superdict[element.strip()])['position'])
                print posicion
                Matrix[contador,posicion]=1
                Matrix [posicion,contador]=1
            contador=contador+1

    index=0
    for element in Status[:,1]:
        if element == 0:
            Matrix[:,index]=0
            Matrix[index,:]=0
        index = index + 1


    np.savetxt(OutputFile, Matrix, delimiter=' ',newline='\n',fmt='%i')