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

def savestadistics(dictstat,day):

    date = datetime.datetime.fromtimestamp(dictstat['init_time'])
    namefile=date.strftime('%j')+"_"+str(dictstat['init_time'])+".stad"
    print "Created: "+namefile

    with open(conf.data_process_stadistics_folder+namefile, 'w+') as outfile:

        line=str(dictstat['init_time'])+";"+str(dictstat['end_time'])+";"+str(day)
        outfile.write(line)

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
        line=str(dictstat['day_mean'])+";"+str(dictstat['day_var'])
        line+="\n"
        outfile.write(line)

    outfile.close()




def run_main():

    matrixdata = []
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
                print init_time
                step_matrix.append([counter,init_time,end_time])
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
                matrixdata=arraydata
                primero=False
            else:
                matrixdata=np.vstack((matrixdata,arraydata))

            if(counter==step_matrix[day][0]):
                #Make stadistics

                #mean sigma by row , all stations in the slot
                slot_day_mean=matrixdata.mean(axis=1)
                slot_day_var=matrixdata.var(axis=1)

                #mean sigma by column , one stations in one day
                stations_mean_day=matrixdata.mean(axis=0)
                stations_var_day=matrixdata.var(axis=0)

                #all stations all day slots
                day_mean=matrixdata.mean()
                day_var=matrixdata.var()

                dictstat = {'init_time':step_matrix[day][1], 'end_time': step_matrix[day][2], 'slot_day_mean': slot_day_mean,\
                            'slot_day_var': slot_day_var,'stations_mean_day': stations_mean_day, 'stations_var_day': stations_var_day,\
                            'day_mean': day_mean,'day_var': day_var}

                #stadistics_matrix.append(dictstat)
                savestadistics(dictstat,day)
                dictstat ={}
                day+=1
                primero=True

            counter+=1
            if(day==len(step_matrix)):
                break


    f.close()
