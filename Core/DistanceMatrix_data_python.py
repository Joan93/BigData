#!/usr/bin/env python

#title           :GetTrafficMatrix.py
#description     :This script process PReMatrix file to get Adjacent matrix of netwok.
#author          :Lucia & Rodrigo
#date            :2016-05-06
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.6
#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================

import config as conf
import numpy as np
import math
import IdDictionary

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

def run_main():
    [superdict,superlista] = IdDictionary.run_main()
    OutputFile_distance = conf.data_process_file_distancematrix
    OutputFile_height = conf.data_process_file_heightmatrix
    OutputFile_inclination = conf.data_process_file_inclination_matrix

    number_stations=465
    alt_matrix=np.zeros((number_stations, number_stations))
    distance_matrix=np.zeros((number_stations, number_stations))
    i=0

    #distance and height alt_matrix
    for i in range (1,number_stations):
        for j in range (i+1,number_stations):
            lon1=float(superlista[i]['long'])
            lat1=float(superlista[i]['lat'])
            height1=float(superlista[i]['alt'])

            lon2=float(superlista[j]['long'])
            lat2=float(superlista[j]['lat'])
            height2=float(superlista[j]['alt'])

            distance = Cal_distance(lon1,  lat1,   lon2,  lat2)
            height = Cal_Height(height1, height2)
            distance_matrix[i,j]=distance
            distance_matrix[j,i]=distance
            alt_matrix[i,j]=height
            alt_matrix[j,i]=-height


    # minval=np.min(distance_matrix[np.nonzero(distance_matrix)])
    # print("minimal distance value: "+str(minval)) #mayor distancia entre dos estaciones: 11.385 km
    # print("max denivel value: "+str(np.amax(alt_matrix))) #mayor desnivel: 138 metros sobre el nivel del mar
    #
    # i,j=np.unravel_index(alt_matrix.argmax(),alt_matrix.shape)
    # print(alt_matrix[i,j])
    # print(distance_matrix[i,j])

    #inclinacion
    np.seterr(divide='ignore', invalid='ignore')
    inclination= np.divide(alt_matrix, distance_matrix)
    inclination[inclination == np.inf] = 0


    np.savetxt(OutputFile_distance, distance_matrix, delimiter=' ',newline='\n',fmt='%i')
    np.savetxt(OutputFile_height, alt_matrix, delimiter=' ',newline='\n',fmt='%i')
    np.savetxt(OutputFile_inclination, np.nan_to_num(inclination), delimiter=' ',newline='\n',fmt='%f')
