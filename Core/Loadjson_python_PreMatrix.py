#!/usr/bin/env python

#title           :LoadJson_python.py
#description     :This script is to ..

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

import os
import json
import geocoder
import time
import config as conf
import codecs

def getaltitude(latitude, longitude):

    print latitude
    print longitude
    h = geocoder.elevation([latitude,longitude]).meters
    time.sleep(0.25)
    return str(h)


def run_main():

    files = os.listdir(conf.data_folder)
    data_process_file_prematrix = conf.data_process_file_prematrix
    data_process_file_vector = conf.data_process_file_vector


    #fichero JSON con el que vamos a trabajar
    with open(conf.data_folder+"/"+files[1]) as data_file:
        data = json.load(data_file)

    f = codecs.open(data_process_file_prematrix, 'w+',encoding='utf8')
    vector_line=""

    for i in xrange(len(data["stations"])):

        f.write(data["stations"][i]["id"])
        f.write(";")
        f.write(data["stations"][i]["streetName"]+" "+data["stations"][i]["streetNumber"])
        f.write(";")
        height =getaltitude(float(data["stations"][i]["latitude"]), float(data["stations"][i]["longitude"]))
        f.write(height)
        f.write(";")
        f.write(data["stations"][i]["latitude"])
        f.write(";")
        f.write(data["stations"][i]["longitude"])
        f.write(";")
        f.write(data["stations"][i]["nearbyStations"])
        f.write(";")
        f.write(data["stations"][i]["type"])
        f.write(";")
        f.write(data["stations"][i]["status"]+";\n")
        vector_line+=data["stations"][i]["id"]+";"+data["stations"][i]["latitude"]+";"+data["stations"][i]["longitude"]+";"+str(height)+";"+str(int(data["stations"][i]["slots"])+int(data["stations"][i]["bikes"]))+";"+data["stations"][i]["type"]+";\n"

    f.close()

    f = codecs.open(data_process_file_vector, 'w+',encoding='utf8')
    f.write(vector_line)
    f.close()
