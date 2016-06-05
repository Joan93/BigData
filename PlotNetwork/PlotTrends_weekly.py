# Estaba funcionando pero ahora genera error


import matplotlib.pyplot as plt
import matplotlib.dates as dte
import networkx as nx
import numpy as np
import time
import fileinput
import os
import re
from datetime import datetime,date, time, timedelta
import calendar
import pylab

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

for a in range (0,2):
    print a



# degree_sequence=[1,5,9,10,2,6,7]
# time_sequence=["a","b","c","d","e","f","g"]
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
    ListOfRealTime2=[]

    with open(FolderPath + file, "r") as fid:
        for line in fid:
            f = line.split(' ')
            # print f
            element=f[0]
            # for element in f:
            g = element.split(';')
                # print len(g)
            if len(g) > 1:
                FirstElement=long(g[0])

    fid.close()

    initialTime=datetime.fromtimestamp(FirstElement)
    print "timestamp:" + str(initialTime)

    Primerdia=datetime.fromtimestamp(FirstElement).weekday()
    print "el indice del primer dia es: " +str(Primerdia)

    Start=initialTime-timedelta(days=Primerdia)
    StartIndex=Start.weekday()
    Year=Start.year
    Month=Start.month
    Day=Start.day

    StartAgain=datetime(Year, Month, Day, 00, 00)

    Accumulative=StartAgain
    while Accumulative < initialTime:
        Accumulative=Accumulative+timedelta(minutes=3)
        print Accumulative
        ListOfRealTime2.append(Accumulative)
        ListOfRealTime.append(Accumulative)
        ListOfBicycles.append(0)

    print "bbbbbbbbb"
    with open(FolderPath+file,"r") as fid:
        for line in fid:
            f = line.split(' ')
            #print f
            for element in f:
                g=element.split(';')
                #print len(g)
                if len(g)>1:
                    #ListOfTimes.append(int(g[1]))
                    elemento=datetime.fromtimestamp(long(g[0]))
                    print " Dentro del archivo" + str(elemento)
                    ListOfRealTime2.append(str(datetime.fromtimestamp((g[0]))))
                    ListOfRealTime.append(g[0])
                    ListOfBicycles.append(int(g[2]))
    fid.close()

    print "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"


    print len(ListOfRealTime), len(ListOfBicycles)

    plt.plot(ListOfRealTime2, ListOfBicycles)
    plt.title(file)
    plt.grid()

        #print "aaaaaaaa"

    #print len(ListOfBicycles),len(ListOfRealTime), len(ListOfTimes)


    #plt.savefig("/home/ns3/Documents/BicingProject/BigData/PlotNetwork/StationGraphs/Bicycle_usage_"+file +".png")
    #print "File " +file+".png saved"
    #plt.close()    #plt.show()


