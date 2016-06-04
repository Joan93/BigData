import matplotlib.pyplot as plt
import matplotlib.dates as dte
import networkx as nx
import numpy as np
import time

from datetime import datetime

ListOfTimes =[]
ListOfBicycles=[]
ListOfRealTime=[]
ListOfSlots=[]

# degree_sequence=[1,5,9,10,2,6,7]
# time_sequence=[0,2,3,4,5,6,8]
# plt.plot(time_sequence,degree_sequence)
# # plt.xlabel(time_sequence)
# plt.show()

with open("/home/ns3/Documents/BicingProject/BigData/Process_Data/Station/389.dat","r") as fid:
    for line in fid:
        f = line.split(' ')
        print f
        for element in f:
            g=element.split(';')
            print len(g)
            if len(g)>1:
                ListOfTimes.append(int(g[1]))
                ListOfBicycles.append(int(g[2]))

print ListOfBicycles
print ListOfTimes

for element in ListOfTimes:
    #dia=int(element/1000)
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
    print cadena

    #tiempo2=datetime.strptime("2012/may/31 00:00", "%Y/%b/%d %H:%M")
    print tiempo2
    #tiempo = datetime.strptime(str(cadena), "%Y/%b/%d %H:%M")

    print cadena, tiempo2
    ListOfRealTime.append(tiempo2)



    #ListOfSlots.append(minute)

    #print dia
    #print ListOfSlots
    #print minute
    #print hora, minuto
    #print element
    print "aaaaaaaa"
    #print hora


print len(ListOfBicycles),len(ListOfRealTime), len(ListOfTimes)

    #dates = dte.num2date(ListOfRealTime)
    #print dates

#dates = dte.date2num(ListOfRealTime)
# plt.plot_date(ListOfRealTime, ListOfBicycles, xdate=True, ydate=False)
# plt.show()
# x = np.array((ListOfRealTime))
# plt.plot(x,ListOfBicycles)
# plt.show()

plt.plot(ListOfRealTime, ListOfBicycles)
plt.gcf().autofmt_xdate()
plt.show()

#plt.plot(ListOfRealTime,ListOfBicycles)
#plt.gcf().autofmt_xdate()
#plt.show()