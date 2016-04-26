#!/usr/bin/env python

#title           :LoadJson_python.py
#description     :This script is to ..

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo


import json
import datetime

from pprint import pprint


#fichero JSON con el que vamos a trabajar
with open('Data/03-17-2016_12:57.json') as data_file:
    data = json.load(data_file)
time=data["updateTime"]


#fichero donde guardamos los nuevos datos
f = open("Process_Data/data_python.txt", 'w+')
hora=datetime.datetime.fromtimestamp(time).strftime('%H')
min=datetime.datetime.fromtimestamp(time).strftime('%M')

dia = datetime.datetime.fromtimestamp(time).weekday()

newdia=dia*1000
newhora=int(hora)*60

horasmin=(int(min)+int(newhora))/3


totaltime=newdia+horasmin

first = True
for i in xrange(len(data["stations"])):

    if(first):
        f.write(str(data["updateTime"])+" ")
        f.write(str(totaltime)+"\n")
        f.write(data["stations"][i]["id"])
        f.write(" ")
        f.write(data["stations"][i]["altitude"])
        f.write(" ")
        f.write(data["stations"][i]["latitude"])
        f.write(" ")
        f.write(data["stations"][i]["bikes"])
        f.write(" ")
        f.write(data["stations"][i]["slots"])
        f.write(" ")
        f.write(data["stations"][i]["type"])
        f.write(" ")
        f.write(data["stations"][i]["status"]+"\n")
        first=False
    else:
        f.write(data["stations"][i]["id"])
        f.write(" ")
        f.write(data["stations"][i]["altitude"])
        f.write(" ")
        f.write(data["stations"][i]["latitude"])
        f.write(" ")
        f.write(data["stations"][i]["bikes"])
        f.write(" ")
        f.write(data["stations"][i]["slots"])
        f.write(" ")
        f.write(data["stations"][i]["type"])
        f.write(" ")
        f.write(data["stations"][i]["status"]+"\n")

