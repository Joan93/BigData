#!/usr/bin/env python

#title           :LoadJson_python.py
#description     :This script is to ..

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

import os
import json
import datetime

from pprint import pprint

path = os.getcwd()+"/Data"
files = os.listdir(path)
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
    f = open(os.getcwd()+"/Process_Data/Python/"+line+".txt", 'w+')




    first = True
    for i in xrange(len(data["stations"])):

        if(first):
            f.write(str(data["updateTime"])+" ")
            f.write(str(totaltime)+"\n")
            f.write(data["stations"][i]["id"])
            f.write(" ")

            '''
            f.write(data["stations"][i]["altitude"])
            f.write(" ")
            f.write(data["stations"][i]["latitude"])
            f.write(" ")
            f.write(data["stations"][i]["longitude"])
            f.write(" ")
            '''

            f.write(data["stations"][i]["bikes"]+"\n")
            '''
            f.write(" ")
            f.write(data["stations"][i]["slots"])
            f.write(" ")
            f.write(data["stations"][i]["type"])
            f.write(" ")
            f.write(data["stations"][i]["status"]+"\n")
            '''
            first=False
        else:
            f.write(data["stations"][i]["id"])
            f.write(" ")
            '''
            f.write(data["stations"][i]["altitude"])
            f.write(" ")
            f.write(data["stations"][i]["latitude"])
            f.write(" ")
            f.write(data["stations"][i]["longitude"])
            f.write(" ")
            '''
            f.write(data["stations"][i]["bikes"]+"\n")
            '''
            f.write(" ")
            f.write(data["stations"][i]["slots"])
            f.write(" ")
            f.write(data["stations"][i]["type"])
            f.write(" ")
            f.write(data["stations"][i]["status"]+"\n")
            '''

    f.close()
