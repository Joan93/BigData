#!/usr/bin/env python

#title           :demo_Rodrigo.py
#description     :This script is or demo work, avoid git conflicts

# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

script_file = "demo_Rodrigo.py"
data_folder = "Data/"
data_process_folder = "Process_Data/RDD/"

# Auto-run Pycharm/python to Spark
import matplotlib.pyplot as plt


print "demo plto by Rodrigo"

vector_x=range(0,10)
vector_string_x=["2^0","2^1","2^2","2^3","2^4","2^5","2^6","2^7","2^8","2^9","2^10"]
vector_y=[1,2,4,8,16,32,64,128,512,1024]

print  vector_x
print  vector_y

plt.xticks(vector_x, vector_string_x)
plt.plot(vector_x,vector_y)
plt.show()