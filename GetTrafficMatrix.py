###################################################################################
#                                                                                 #
#   Obtener la matrix de conectividad en funcion del estado de las estaciones     #
#                                                                                 #
###################################################################################

import numpy as np
from collections import OrderedDict
#import resource

#t_ini=time.time()

NumberOfStations=496
Matrix=np.zeros((NumberOfStations,NumberOfStations))
Status=np.zeros((NumberOfStations,2))

Contador=0
with open("Process_Data/Prematrix_data_python_fix.txt","r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        partners=f[5]
        status=f[7]
        p=partners.split(',')
        Status[int(id) - 1, 0]=id
        if status=="OPN":
            Status[int(id)-1,1]=1
        else:
            Status[int(id)-1,1]=0
        #print id + " " + partners
        #print id
        #print "\n"
        for element in p:
            Matrix[int(id)-1,int(element)-1]=1
            Matrix [int(element)-1,int(id)-1]=1

        #    print element
        #print "\n \n"

index=0
for element in Status[:,1]:
    if element == 0:
        Matrix[:,index]=0
        Matrix[index,:]=0
    index = index + 1

#import io
#g=io.open("Process_Data/RDD/TrafficMatrix_data_python.txt", 'w+', encoding='utf8')
#linea= ""
#for i in range(0,495):
#    print(Matrix[:, i])
    #g.write (Matrix[:, i])
#    print "\n"
#    linea=""

np.savetxt('Process_Data/RDD/TrafficMatrix_data_python_BIG.txt', Matrix, delimiter=' ',newline='\n',fmt='%i')