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


def run_main(file):

    NumberOfStations=465
    print file
    adjmatrix = np.loadtxt(file,delimiter=' ',dtype=np.dtype('int32'))

    # for i in range (0,NumberOfStations):
    #     if(adjmatrix[i,i]==1):
    #         print "posicion: ["+str(i)+","+str(i)+"]"


    g = nx.from_numpy_matrix(adjmatrix, create_using = nx.MultiGraph())
    degree = g.degree()
    density = nx.density(g)
    degree_centrality = nx.degree_centrality(g)
    clossness_centrality = nx.closeness_centrality(g)
    betweenless_centrality = nx.betweenness_centrality(g)

    print degree
    print density
    print degree_centrality
    print clossness_centrality
    print betweenless_centrality
    #nx.draw(g)
#    np.savetxt(OutputFile, Matrix, delimiter=' ',newline='\n',fmt='%i')