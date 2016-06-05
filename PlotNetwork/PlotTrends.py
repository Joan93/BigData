import matplotlib.pyplot as plt
import matplotlib.dates as dte
import networkx as nx
import numpy as np
import time
import fileinput
import os
import re
from datetime import datetime

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split('(\d+)', text)]


ListOfTimes =[]
ListOfBicycles=[]
ListOfRealTime=[]
ListOfSlots=[]

# degree_sequence=[1,5,9,10,2,6,7]
# time_sequence=[0,2,3,4,5,6,8]
# plt.plot(time_sequence,degree_sequence)
# # plt.xlabel(time_sequence)
# plt.show()

FolderPath="/home/ns3/Documents/BicingProject/BigData/Process_Data/Station/"

files = [f for f in os.listdir(FolderPath) if f.endswith(".dat")]
files.sort(key=natural_keys)
for file in files:

    ListOfTimes = []
    ListOfBicycles = []
    ListOfRealTime = []
    ListOfSlots = []

    with open(FolderPath+file,"r") as fid:
        for line in fid:
            f = line.split(' ')
            #print f
            for element in f:
                g=element.split(';')
                #print len(g)
                if len(g)>1:
                    ListOfTimes.append(int(g[1]))
                    ListOfBicycles.append(int(g[2]))
    fid.close()

    #print ListOfBicycles
    #print ListOfTimes

    for element in ListOfTimes:
        dia,slot=divmod(element,1000)
        minute=slot*3
        hora,minuto=divmod(minute,60)
        tiempo2=datetime(2012, 5, dia, hora, minuto)
        if hora<10:
            hora="0"+str(hora)
        if minuto<10:
            minuto="0"+str(minuto)
        if dia<10:
            dia="0"+str(dia)
        cadena="2012/12/"  + str(dia)+ " " + str(hora) + ":" + str(minuto)
        #print cadena
        #print tiempo2
        #print cadena, tiempo2
        ListOfRealTime.append(tiempo2)

        #print "aaaaaaaa"

    #print len(ListOfBicycles),len(ListOfRealTime), len(ListOfTimes)

    plt.plot(ListOfRealTime, ListOfBicycles)
    plt.gcf().autofmt_xdate()
    plt.title(file)
    plt.grid()
    plt.savefig("/home/ns3/Documents/BicingProject/BigData/PlotNetwork/StationGraphs/Bicycle_usage_"+file +".png")
    print "File " +file+".png saved"
    plt.close()    #plt.show()
