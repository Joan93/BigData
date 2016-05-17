###################################################################################
#                                                                                 #
#   Obtener la matrix de conectividad en funcion del estado de las estaciones     #
#                                                                                 #
###################################################################################

import numpy as np
from collections import OrderedDict
#import resource

#t_ini=time.time()

NumberOfStations=465
Matrix=np.zeros((NumberOfStations,NumberOfStations))
Status=np.zeros((NumberOfStations,2))

contador=0
with open("Process_Data/Prematrix_data_python_fix.txt","r") as fid:
    for line in fid:
        f=line.split(';')
        id=f[0]
        partners=f[5]
        status=f[7]
        p=partners.split(',')
        Status[contador, 0]=id
        if status=="OPN":
            Status[contador,1]=1
        else:
            Status[contador,1]=0
        #print id + " " + partners
        #print id
        #print "\n"
        for element in p:
            Matrix[contador,int(element)-1]=1
            Matrix [int(element)-1,contador]=1

        contador=contador+1

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