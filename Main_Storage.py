#!/usr/bin/env python

#title           :Main_Storage.py
#description     :This script is the main that call the rest of script to run the project base on storage info.
#author          :Rodrigo
#date            :2016-04-19
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.6
#requirements    :Internet conexion, Spark 1.6, numpy, geocoder

#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================

print("******************************************")
print("#         Bigdata Bicing Barcelona       #")
print("******************************************")
print("******************************************")
print("#  Version 0.1 20/05/2016 MASTEAM-EETAC  #")
print("******************************************")
print("\n")

# Import the config file, folder, files and configurations parameters
import config as conf

if(conf.mode_test):
    print ("** Config Show ***\n")
    print ("-- Spark path:")
    print(conf.spark_path+"\n")
    print ("-- Log error:")
    print(conf.log_error_file+"\n")
    print ("-- Core Folder:")
    print(conf.core_folder+"\n")
    print ("-- Data Folder:")
    print(conf.data_folder+"\n")
    print ("-- Process Data Folder:")
    print(conf.data_process_folder)
    print ("--* SuperFile Folder:")
    print(conf.data_process_folder_superfile)
    print ("--* Superstation Folder:")
    print(conf.data_process_folder_station+"\n")

if(conf.spark_use):
    import  Core.LoadJson_to_RDD
    import Core.LoadJson_to_RDD_PreMatrix
else:
    import Core.LoadJson_python
    import Core.Loadjson_python_PreMatrix

#Process the Json storage to compact in a historical data files
#Json2ProcessData.main()