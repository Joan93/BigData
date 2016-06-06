#!/usr/bin/env python

#title           :ProcessData.py
#description     :This script process json files from Barcelona Bicing, filtering and storage in a better form.
#author          :Rodrigo
#date            :2016-04-19
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.6
#requirements    :Spark 1.6
#==============================================================================
#==============================================================================
# UPC-EETAC MASTEAM 2015-2016 BIGDATA                                         #
# Group former by Ana, Lucia, Joan and Rodrigo                                #
#==============================================================================
import config as conf
import numpy as np
import datetime


InputFile = conf.data_process_folder_superfile_file_data
InputFile_header = conf.data_process_folder_superfile_file_header
Stadistics_Folder=conf.data_process_stadistics_folder

def savestadistics(dictstat,day,type):
    if(type==0):
        date = datetime.datetime.fromtimestamp(dictstat['init_time'])
        namefile=date.strftime('%j')+"_"+str(dictstat['init_time'])+".stad"

    else:
        if(day==-1):
            tipo="working"
        elif(day==-2):
            tipo="weekend"
        else:
            tipo="all"

        namefile="Total_"+tipo+"_"+str(dictstat['init_time'])+".stad"

    print "Created: "+namefile
    with open(conf.data_process_stadistics_folder+namefile, 'w+') as outfile:

        line=str(dictstat['init_time'])+";"+str(dictstat['end_time'])+";"+str(day)
        line+="\n"
        outfile.write(line)

        if(type==0 or type==2):
            line=""
            primercon=True
            for slot_day_mean in dictstat['slot_day_mean']:

                if(primercon):
                    line+=str(slot_day_mean)
                    primercon=False
                else:
                    line+=" "+str(slot_day_mean)
            line+="\n"
            outfile.write(line)

            line=""
            primercon=True
            for slot_day_var in dictstat['slot_day_var']:

                if(primercon):
                    line+=str(slot_day_var)
                    primercon=False
                else:
                    line+=" "+str(slot_day_var)
            line+="\n"
            outfile.write(line)

        line=""
        primercon=True
        for stations_mean_day in dictstat['stations_mean_day']:

            if(primercon):
                line+=str(stations_mean_day)
                primercon=False
            else:
                line+=" "+str(stations_mean_day)
        line+="\n"
        outfile.write(line)

        line=""
        primercon=True
        for stations_var_day in dictstat['stations_var_day']:

            if(primercon):
                line+=str(stations_var_day)
                primercon=False
            else:
                line+=" "+str(stations_var_day)
        line+="\n"
        outfile.write(line)
        line=str(dictstat['day_mean'])+" "+str(dictstat['day_var'])
        line+="\n"
        outfile.write(line)

    outfile.close()




def run_main():

    daydata = []
    matrixdata = []
    weekdaydata = []
    weekenddaydata = []
    header_vector = []
    step_matrix = []
    stadistics_matrix = []

    # #process each line
    # primero=True
    # with open(InputFile) as f:
    #     for line in f:
    #         line.rstrip('\n')
    #         splitarray=line.split(" ")
    #         time = splitarray[0].split(";")[0]
    #         pseudotime = splitarray[0].split(";")[1]
    #         arraydata =  np.array(splitarray[1:len(splitarray)], dtype=int)
    #
    #         if(primero):
    #             matrixdata=arraydata
    #             primero=False
    #         else:
    #             matrixdata=np.vstack((matrixdata,arraydata))
    #
    # f.close()

    #process each line

    primero=True
    primero_init=True
    with open(InputFile_header) as f:
        counter=0
        day=0
        for line in f:
            line.rstrip('\n')
            arraydata =  np.array(line.split(";"), dtype=int)
            dia,slot=divmod(arraydata[1],1000)

            if(primero):
                old_day=dia
                primero=False
            if(primero_init):
                init_time = arraydata[0]
                primero_init=False

            dict = {'time':arraydata[0], 'pseudotime': arraydata[1], 'day': dia, 'slot': slot}
            header_vector.append([counter,dict,day])

            if(old_day!=dia):
                primero_init=True
                old_day=dia
                end_time = arraydata[0]
                #print init_time
                step_matrix.append([counter,init_time,end_time,dia])
                day+=1

            counter+=1

            # if(counter==703):
            #     break

    f.close()

    primero=True
    counter=0
    day=0
    with open(InputFile) as f:
        for line in f:
            line.rstrip('\n')
            arraydata =  np.array(line.split(" "), dtype=int)

            if(primero):
                daydata=arraydata
                matrixdata=arraydata
                primero=False
            else:
                daydata=np.vstack((daydata,arraydata))
                matrixdata=np.vstack((matrixdata,arraydata))


            if(step_matrix[day][3]<5):
                if (len(weekdaydata)==0):
                    weekdaydata=arraydata
                else:
                    weekdaydata=np.vstack((weekdaydata,arraydata))


            if(step_matrix[day][3]>4):
                if (len(weekenddaydata)==0):
                    weekenddaydata=arraydata
                else:
                    weekenddaydata=np.vstack((weekenddaydata,arraydata))

            if(counter==step_matrix[day][0]):
                #Make stadistics

                #mean sigma by row , all stations in the slot
                slot_day_mean=daydata.mean(axis=1)
                slot_day_var=daydata.var(axis=1)

                #mean sigma by column , one stations in one day
                stations_mean_day=daydata.mean(axis=0)
                stations_var_day=daydata.var(axis=0)

                #all stations all day slots
                day_mean=daydata.mean()
                day_var=daydata.var()

                dictstat = {'init_time':step_matrix[day][1], 'end_time': step_matrix[day][2], 'slot_day_mean': slot_day_mean,\
                            'slot_day_var': slot_day_var,'stations_mean_day': stations_mean_day, 'stations_var_day': stations_var_day,\
                            'day_mean': day_mean,'day_var': day_var}

                #stadistics_matrix.append(dictstat)
                savestadistics(dictstat,day,0)
                dictstat ={}
                day+=1
                primero=True

            counter+=1
            if(day==len(step_matrix)):
                break


    f.close()

    #*Stadistics working day

    #mean sigma by column , one stations in one day
    all_stations_mean_day=weekdaydata.mean(axis=0)
    all_stations_var_day=weekdaydata.var(axis=0)

    #all stations all day slots
    all_days_mean=weekdaydata.mean()
    all_days_var=weekdaydata.var()

    dictstat = {'init_time':step_matrix[0][1], 'end_time': step_matrix[day-1][2], 'stations_mean_day': all_stations_mean_day, 'stations_var_day': all_stations_var_day,\
                'day_mean': all_days_mean,'day_var': all_days_var}

    savestadistics(dictstat,-1,1)

    dictstat ={}

    #*Stadistics weekend day

    #mean sigma by column , one stations in one day
    all_stations_mean_day=weekenddaydata.mean(axis=0)
    all_stations_var_day=weekenddaydata.var(axis=0)

    #all stations all day slots
    all_days_mean=weekenddaydata.mean()
    all_days_var=weekenddaydata.var()

    dictstat = {'init_time':step_matrix[0][1], 'end_time': step_matrix[day-1][2], 'stations_mean_day': all_stations_mean_day, 'stations_var_day': all_stations_var_day,\
                'day_mean': all_days_mean,'day_var': all_days_var}

    savestadistics(dictstat,-2,1)
    dictstat ={}

    #*All stadistics
    #mean sigma by row , all stations in the slot
    all_slot_day_mean=matrixdata.mean(axis=1)
    all_slot_day_var=matrixdata.var(axis=1)
    #mean sigma by column , one stations in one day
    all_stations_mean_day=matrixdata.mean(axis=0)
    all_stations_var_day=matrixdata.var(axis=0)

    #all stations all day slots
    all_days_mean=matrixdata.mean()
    all_days_var=matrixdata.var()

    dictstat = {'init_time':step_matrix[0][1], 'end_time': step_matrix[day-1][2],'slot_day_mean': all_slot_day_mean, \
                'slot_day_var': all_slot_day_var, 'stations_mean_day': all_stations_mean_day, \
                'stations_var_day': all_stations_var_day, 'day_mean': all_days_mean,'day_var': all_days_var}

    savestadistics(dictstat,-3,2)

    import math

    vector_y_plus2sigma=[]
    vector_y_less2sigma=[]
    vector_y_mean=[]
    vector_y_mean_Total=[]
    vector_y_Total_plus2sigma=[]
    vector_y__Totaless2sigmal=[]
    vector_x=range(0,len(all_slot_day_mean))

    for slot in range(0,len(all_slot_day_mean)):
        print "slot: "+str(slot)+" mean: "+str(all_slot_day_mean[slot])+ " - sigma: "+str(math.sqrt(all_slot_day_var[slot]))
        vector_y_mean.append(all_slot_day_mean[slot])
        vector_y_plus2sigma.append(all_slot_day_mean[slot]+math.sqrt(all_slot_day_var[slot]))
        vector_y_less2sigma.append(all_slot_day_mean[slot]-math.sqrt(all_slot_day_var[slot]))
        vector_y_mean_Total.append(all_days_mean)

    import matplotlib.pyplot as plt

    print "empezando hacer graficas"
    plt.close("all")
    plt.rc('xtick', labelsize=8)

    fig=plt.figure()
    fig.set_size_inches(20, 8)
    fig.suptitle('Mean Bike in Bicing ', fontsize=22, fontweight='bold')

    plt.plot(vector_x,vector_y_mean,'b')
    plt.plot(vector_x,vector_y_mean_Total,'g')
    plt.plot(vector_x,vector_y_plus2sigma,'r--')
    plt.plot(vector_x,vector_y_less2sigma,'r--')


    fig.savefig('Memoria_data.jpg',dpi = 100)
    plt.show()

    plt.close("all")
    plt.rc('xtick', labelsize=8)

    fig=plt.figure()
    fig.set_size_inches(20, 8)


    fig.suptitle('Mean Bike in Station ', fontsize=22, fontweight='bold')

    vector_y_plus2sigma=[]
    vector_y_less2sigma=[]
    vector_y_mean=[]
    vector_x=range(0,len(all_stations_mean_day))

    for slot in range(0,len(all_stations_mean_day)):
        print "slot: "+str(slot)+" mean: "+str(all_stations_mean_day[slot])+ " - sigma: "+str(math.sqrt(all_stations_var_day[slot]))
        vector_y_mean.append(all_stations_mean_day[slot])
        vector_y_plus2sigma.append(all_stations_mean_day[slot]+math.sqrt(all_stations_var_day[slot]))
        vector_y_less2sigma.append(all_stations_mean_day[slot]-math.sqrt(all_stations_var_day[slot]))
        vector_y_mean_Total.append(all_days_mean)



    plt.plot(vector_x,vector_y_mean,'b')
    plt.plot(vector_x,vector_y_mean_Total,'g')
    plt.plot(vector_x,vector_y_plus2sigma,'r--')
    plt.plot(vector_x,vector_y_less2sigma,'r--')


    fig.savefig('Memoria_data_stations.jpg',dpi = 100)
    plt.show()



