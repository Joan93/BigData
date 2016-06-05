#!/usr/bin/env python

#title           :demo_Rodrigo.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

script_file = "demo_Rodrigo.py"
data_folder = "Data/"
data_process_folder = "Process_Data/RDD/"

# Auto-run Pycharm/python to Spark
import sys
import os
import datetime

your_timestamp = 1458215648
date = datetime.datetime.fromtimestamp(your_timestamp)
print date

day_of_year = date.strftime('%j')

print day_of_year