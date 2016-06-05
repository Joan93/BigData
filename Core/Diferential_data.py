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
import numpy as np
import config as conf


data_process_folder_superfile = conf.data_process_folder_superfile_file_data
data_process_folder_superfile_diferential= conf.data_process_folder_superfile+"superfile_diferential.dat"

def run_main():
    print "Cargando"
    superfile= np.loadtxt(data_process_folder_superfile,delimiter=' ', dtype=np.dtype('int32'))

    print superfile.shape[0]
    print superfile.shape[1]
    diferential_matrix=np.zeros((superfile.shape[0], superfile.shape[1]))

    for i in range(0,superfile.shape[0]):
        for j in range(0,superfile.shape[1]):
            if(j==0):
                diferential_matrix[i,j]=0
            else:
                diferential_matrix[i,j]=superfile[i,j]-superfile[i,j-1]


    np.savetxt(data_process_folder_superfile_diferential, diferential_matrix, delimiter=' ',newline='\n',fmt='%i')