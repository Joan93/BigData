#!/usr/bin/env python

#title           :LoadJson_python.py
#description     :This script is to ..

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

import os
import json
import datetime
from pprint import pprint
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



    #fichero JSON con el que vamos a trabajar
    with open(conf.data_folder+"/"+files[1]) as data_file:
        data = json.load(data_file)

    f = codecs.open(data_process_file_prematrix, 'w+',encoding='utf8')


    first = True
    for i in xrange(len(data["stations"])):

        f.write(data["stations"][i]["id"])
        f.write(";")
        f.write(data["stations"][i]["streetName"]+" "+data["stations"][i]["streetNumber"])
        f.write(";")
        f.write(getaltitude(float(data["stations"][i]["latitude"]), float(data["stations"][i]["longitude"])))
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

    f.close()
