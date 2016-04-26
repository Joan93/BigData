import numpy as np
from collections import OrderedDict
#import resource

#t_ini=time.time()

NumberOfStations=496
Matrix=np.zeros((NumberOfStations,NumberOfStations))

Contador=0
with open("Process_Data/RDD/Prematrix_data_python.txt","r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        partners=f[5]
        p=partners.split(',')
        #print id + " " + partners
        #print id
        #print "\n"
        for element in p:
            Matrix[int(id)-1,int(element)-1]=1
            Matrix [int(element)-1,int(id)-1]=1
        #    print element
        #print "\n \n"

#import io
#g=io.open("Process_Data/RDD/TrafficMatrix_data_python.txt", 'w+', encoding='utf8')
#linea= ""
#for i in range(0,495):
#    print(Matrix[:, i])
    #g.write (Matrix[:, i])
#    print "\n"
#    linea=""

np.savetxt('Process_Data/RDD/TrafficMatrix_data_python.txt', Matrix, delimiter=' ',newline='\n',fmt='%i')