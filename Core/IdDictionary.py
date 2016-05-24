#!/usr/bin/env python

#title           :IdDictionary.py
#description     :This script helt to other givin a dictionary ID -> position in matrix
#author          :Rodrigo Sampedro
#date            :2016-05-24
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.6
#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================

import config as conf

def run_main():
    vector_data_file = conf.data_process_file_vector
    dict_of_dict_byid = {}
    lista_staciones=[]

    with open(vector_data_file,"r") as fid:
        contador=0
        for line in fid:
            elementdict ={}
            f=line.split(';')
            elementdict['id']=f[0]
            elementdict['lat']=f[1]
            elementdict['long']=f[2]
            elementdict['alt']=f[3]
            elementdict['total']=f[4]
            elementdict['type']=f[5]
            elementdict['position']=contador
            dict_of_dict_byid[f[0]]=elementdict
            lista_staciones.append(elementdict)
            contador+=1

    return [dict_of_dict_byid,lista_staciones]