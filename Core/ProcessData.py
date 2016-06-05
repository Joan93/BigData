#!/usr/bin/env python

#title           :ProcessData.py
#description     :This script process json files from Barcelona Bicing, filtering and storage in a better form.
#author          :Rodrigo
#date            :2016-04-19
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.6
#requirements    :Spark 1.6
#==============================================================================
#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================


# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

# Auto-run Pycharm/python to Spark
import sys
import os
import re
import numpy as np
import config as conf



data_folder = conf.data_process_historical
data_process_folder_superfile = conf.data_process_folder_superfile
data_process_folder_station = conf.data_process_folder_station


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split('(\d+)', text)]

def run_main():
    #Load data
    #files = os.listdir(data_folder)
    files = [f for f in os.listdir(data_folder) if f.endswith(".txt")]
    vector = []
    labelcolumn = []
    files.sort(key=natural_keys)

    for file in files:

        vector = np.array([])

        #process file name
        path = data_folder+file
        #Get the timestamp and pseudotime
        time = file[:-4].split('_')
        pseudotime = time[1]
        timestamp= time[0]

        #vector = np.append(vector, [timestamp,pseudotime])
        #for a in vector:
        #    print a;

        #process each line
        with open(data_folder+file) as f:
            for line in f:
                id = line.split(" ")[0]
                bikes = line.split(" ")[1].rstrip('\n')
                #print ("file:"+file+" "+id+" "+bikes)
                #Write bikes value in station.dat file
                fw = open(data_process_folder_station+id+".dat","a+")
                line = str(timestamp)+";"+str(pseudotime)+";"+str(bikes)+" "
                #print line
                fw.write(line.rstrip('\n'))
                fw.close()

                vector = np.append(vector, bikes)

        #Write Time vector for all ID in file
        fw = open(conf.data_process_folder_superfile_file_data,"a+")
        #Write header data file
        fw2 = open(conf.data_process_folder_superfile_file_header,"a+")
        line=""

        #print vector
        primercaso=True
        for x in np.nditer(vector):
            if(primercaso):
                line+=str(x)
                primercaso=False
            else:
                line+=" "+str(x)

        #line = str(timestamp)+";"+str(pseudotime)+" "+str(line)+"\n"
        line = str(line)+"\n"
        fw2.write(str(timestamp)+";"+str(pseudotime)+"\n")
        fw2.close()
        fw.write(line)
        fw.close()

    import fileinput
    files = [f for f in os.listdir(data_process_folder_station) if f.endswith(".dat")]
    files.sort(key=natural_keys)
    with open(conf.data_process_folder_superfile_filestation, 'w') as outfile:
        for fname in files:
            #print fname
            with open(data_process_folder_station+fname) as infile:
                outfile.write(infile.read()+"\n")

    outfile.close()