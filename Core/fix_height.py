#!/usr/bin/env python

#title           :LoadJson_python.py
#description     :This script is to ..

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

import geocoder
import time
import config as conf
import io

def fix():
    prematrix_file = conf.data_process_file_prematrix
    heigth=[]
    fw = open(conf.data_process_file_prematrix,"w+")
    i=0
    #Open file an fix altitude of each station
    with open(conf.data_process_file_prematrix_error,) as f:

        for line in f:
            slots = line.split(";")
            # id = slots[0]
            # street = slots[1]
            # heigth = slots[2]
            lat = float(slots[3])
            lon = float(slots[4])
            # neighbours = slots[5]
            # type = slots[6]
            # status = slots[7]

            #print("old height: " + str(heigth))
            #fix heigth
            print [lat,lon]
            altura =geocoder.elevation([lat,lon]).meters
            heigth.append(altura)
            print("Fix height: " + str(heigth[i]))
            print  altura
            time.sleep(0.25)


            line = slots[0]+";"+slots[1]+";"+str(heigth[i])+";"+slots[3]+";"+slots[4]+";"+slots[5]+";"+slots[6]+";"+slots[7]+";\n"
            #print line
            fw.write(line)
            i+=1


    fw.close()
    f.close()

    fw = open(conf.data_process_file_vector,"w+")
    i=0
    #Open file an fix altitude of each station
    with open(conf.data_process_file_vector_error,) as f:

        for line in f:
            slots = line.split(";")
            # id = slots[0]
            line = slots[0]+";"+slots[1]+";"+slots[2]+";"+str(heigth[i])+";"+slots[4]+";"+slots[5]+";\n"
            #print line
            fw.write(line)
            i+=1


    fw.close()
    f.close()