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
import config
import numpy as np
def run_main():

    InputFile = config.data_process_folder_superfile_file_data
    InputFile_header = config.data_process_folder_superfile_file_header
    matrixdata = []

    # #process each line
    # primero=True
    # with open(InputFile) as f:
    #     for line in f:
    #         line.rstrip('\n')
    #         splitarray=line.split(" ")
    #         time = splitarray[0].split(";")[0]
    #         pseudotime = splitarray[0].split(";")[1]
    #         arraydata =  np.array(splitarray[1:len(splitarray)], dtype=int)
    #
    #         if(primero):
    #             matrixdata=arraydata
    #             primero=False
    #         else:
    #             matrixdata=np.vstack((matrixdata,arraydata))
    #
    # f.close()

    #process each line
    primero=True
    with open(InputFile) as f:
        for line in f:
            line.rstrip('\n')
            arraydata =  np.array(line.split(" "), dtype=int)

            if(primero):
                matrixdata=arraydata
                primero=False
            else:
                matrixdata=np.vstack((matrixdata,arraydata))

    f.close()
