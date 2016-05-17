#!/usr/bin/env python

#title           :config.py
#description     :This script is the base of path and folder variables, spark and other utilities.
#author          :Rodrigo
#date            :2016-05-17
#version         :0.1
#python_version  :2.7.6
#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================

import os

# Software Visibility
log_error=True # if the programe save the error in a file
verbose=True # if the program show in screen the status information of the data or process
mode_test=True #try to check some test at init of the program
spark_use=False

#--- External Software:
# *SPARK
spark_path_1_3 = "/home/rodrigo/Programe_Files_Linux/spark-1.3.0-bin-hadoop2.4/bin/spark-submit"
spark_path_1_6 = "/home/rodrigo/Programe_Files_Linux/spark-1.6.1-bin-hadoop2.6/bin/spark-submit"
spark_path = spark_path_1_6 #default spark 1.6 for stadistics


#--- Folder directories structure
project_path = os.getcwd()+"/"

# *Log error File
log_error_file=project_path+"log_error.log"

# *Core Scripts
core_folder =project_path+"Core/"

# *Raw data storage in json from scripts
data_folder = project_path+"Data/"
# *Process data
data_process_folder = project_path+"Process_Data/"
data_process_folder_RDD = project_path+"Process_Data/RDD/"
data_process_folder_python = project_path+"Process_Data/python/"
# *Process Data historical Storage
data_process_historical = project_path+"Process_Data/Data_history/"

# *Super Files subfolder in Process Data
data_process_folder_superfile = project_path+"Process_Data/SuperFile/"
data_process_folder_station = project_path+"Process_Data/Station/"
