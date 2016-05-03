#!/usr/bin/env python

#title           :ProcessData.py
#description     :This script process json files from Barcelona Bicing, filtering and storage in a better form.
#author          :Rodrigo
#date            :2016-04-19
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.6
#requirements    :Spark 1.3
#==============================================================================


# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

data_folder = "Process_Data/RDD/"
data_process_folder_superfile = "Process_Data/RDD/SuperFile/"
data_process_folder_station = "Process_Data/RDD/Station/"

# Auto-run Pycharm/python to Spark
import sys
import os

# **** Script in SPARK ****

import numpy as np


#Load data
#files = os.listdir(data_folder)
files = [f for f in os.listdir(data_folder) if f.endswith(".txt")]
vector = []
labelcolumn = []

for file in files:

    vector = np.array([])

    #process file name
    path = data_folder+file
    #Get the timestamp and pseudotime
    time = file[:-4].split('_')
    pseudotime = int(time[1])
    timestamp= int(time[0])

    vector = np.append(vector, [timestamp,pseudotime])

    #process each line
    with open(data_folder+file) as f:
        for line in f:
            id = line.split(" ")[0]
            bikes = line.split(" ")[1].rstrip('\n')

            #Write bikes value in station.dat file
            fw = open(data_process_folder_station+id+".dat","a+")
            line = str(timestamp)+";"+str(pseudotime)+";"+str(bikes)+" "
            fw.write(line.rstrip('\n'))
            fw.close()

            vector = np.append(vector, bikes)

    #Write Time vector for all ID in file
    fw = open(data_process_folder_superfile+"superfile.dat","a+")
    line=""

    #print vector
    for x in np.nditer(vector):
        line+=str(x)+" "

    line = str(timestamp)+";"+str(pseudotime)+" "+str(line)+"\n"
    fw.write(line)
    fw.close()

import fileinput
files = [f for f in os.listdir(data_process_folder_station) if f.endswith(".dat")]
with open(data_process_folder_superfile+"superstationfile.dat", 'w') as outfile:
    for fname in files:
        print fname
        with open(data_process_folder_station+fname) as infile:
            outfile.write(infile.read()+"\n")

outfile.close()