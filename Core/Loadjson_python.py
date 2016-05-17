#!/usr/bin/env python

#title           :LoadJson_python.py
#description     :This script process the data in json format to compact interesting data files.
#author          :Joan
#date            :2016-04-12
#version         :0.3
#usage           :python LoadJson_python.py
#notes           :
#python_version  :2.7.6

#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================

import os
import json
import datetime

import config as conf
from pprint import pprint


path = conf.data_folder
path_save = conf.data_process_historical

def run_main(alone):

    if(alone):
        path = os.path.dirname(os.getcwd())+"/"+conf.data
        path_save = os.path.dirname(os.getcwd())+"/"+conf.processdata+"/"+conf.history
    else:
        path = conf.data_folder
        path_save = conf.data_process_historical

    files = os.listdir(path)
    total_files = len(files)
    j=0
    for file in files:
       # data_raw = sc.textFile(path+"/"+file)


        #fichero JSON con el que vamos a trabajar
        with open(path+"/"+file) as data_file:
            data = json.load(data_file)
        time=data["updateTime"]

        hora=datetime.datetime.fromtimestamp(time).strftime('%H')
        min=datetime.datetime.fromtimestamp(time).strftime('%M')

        dia = datetime.datetime.fromtimestamp(time).weekday()

        newdia=dia*1000
        newhora=int(hora)*60

        horasmin=(int(min)+int(newhora))/3


        totaltime=newdia+horasmin


        #fichero donde guardamos los nuevos datos
        #f = open("Process_Data/Python/"+file+".txt", 'w+')

        line= str(time)+"_"+str(totaltime).zfill(4)

        filename = file.split(".")
        f = open(path_save+line+".txt", 'w+')

        first = True

        for i in xrange(len(data["stations"])):

            f.write(data["stations"][i]["id"])
            f.write(" ")
            f.write(data["stations"][i]["bikes"])
            f.write(" ")
            f.write(data["stations"][i]["status"]+"\n")

        if(conf.verbose):
            porcentaje = float(j*100/total_files)
            line_porc="|"
            for m in range(0,int(porcentaje)):
                line_porc+="="
            print line_porc.rstrip('\n')+"| "+str(porcentaje)+"% \n \n \n"
            print("Procesando ... ")

        f.close()

        j+=1


#run_main(True)