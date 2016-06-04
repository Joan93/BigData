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
core = "Core/"
core_folder =project_path+core


# *Raw data storage in json from scripts
data = "Data/"
data_folder = project_path+data
# *Process data
processdata = "Process_Data/"
data_process_folder = project_path+processdata
data_process_folder_RDD = project_path+"Process_Data/RDD/"
data_process_folder_python = project_path+"Process_Data/python/"
# *Process Data historical Storage
history ="Data_history/"
data_process_historical = data_process_folder+history
# *Prematrix fix processing
data_process_file_prematrix=data_process_folder+"Prematrix_data.txt"
data_process_file_prematrix_error=data_process_folder+"Prematrix_data_error.txt"

# *Vector
data_process_file_vector=data_process_folder+"vector_data.txt"
data_process_file_vector_error=data_process_folder+"vector_data_error.txt"

# *Super Files subfolder in Process Data
superfile="SuperFile/"
data_process_folder_superfile = data_process_folder+superfile
superstation="Station/"
data_process_folder_station = data_process_folder+superstation

# *Distance Matrix File
distancematrixfile ="DistanceMatrix.dat"
data_process_file_distancematrix =data_process_folder+distancematrixfile
height_matrixfile ="HeightMatrix.dat"
data_process_file_heightmatrix =data_process_folder+height_matrixfile
inclination_matrixfile ="InclinationMatrix.dat"
data_process_file_inclination_matrix =data_process_folder+inclination_matrixfile


distance_300=300
distance=500
distance_1000=1000
min_neigbours=4

# *Adyacent Matrix File
adjacentmatrixfile ="AdjacentMatrix.dat"
data_process_file_adjacentmatrix =data_process_folder+adjacentmatrixfile
adjacentmatrixfile_distance ="AdjacentMatrix_distance.dat"
data_process_file_adjacentmatrix_distance =data_process_folder+adjacentmatrixfile_distance
adjacentmatrixfile_distance_300 ="AdjacentMatrix_distance_300.dat"
data_process_file_adjacentmatrix_distance_300 =data_process_folder+adjacentmatrixfile_distance_300
adjacentmatrixfile_distance_1000 ="AdjacentMatrix_distance_1000.dat"
data_process_file_adjacentmatrix_distance_1000 =data_process_folder+adjacentmatrixfile_distance_1000
weight_edgematrix ="WeightMatrix.dat"
data_process_file_weight_edgematrix =data_process_folder+weight_edgematrix
weight_edgematrix_1000 ="WeightMatrix_1000.dat"
data_process_file_weight_edgematrix_1000 =data_process_folder+weight_edgematrix_1000
weight_edgematrix_300 ="WeightMatrix_300.dat"
data_process_file_weight_edgematrix_300 =data_process_folder+weight_edgematrix_300
weight_edgematrix_distance ="WeightMatrix_distance.dat"
data_process_file_weight_edgematrix_distance =data_process_folder+weight_edgematrix_distance
weight_edgematrix_ref ="WeightMatrix_ref.dat"
data_process_file_weight_edgematrix_ref =data_process_folder+weight_edgematrix_ref
