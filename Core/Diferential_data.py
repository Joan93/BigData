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



# UPC-EETAC MASTEAM 2015-2016 BIGDATA
# Group former by Ana, Lucia, Joan and Rodrigo

# Auto-run Pycharm/python to Spark
import numpy as np
import config as conf


data_process_folder_superfile = conf.data_process_folder_superfile_file_data
data_process_folder_superfile_diferential= conf.data_process_folder_superfile+"superfile_diferential.dat"
data_process_folder_superfile_header = conf.data_process_folder_superfile_file_header
data_process_folder_plots = conf.data_process_folder_plots

weekday = {0 : "Mon",
           1 : "Tue",
           2 : "Wed",
           3 : "Thu",
           4 : "Fri",
           5 : "Sat",
           6 : "Sun"
}


def run_main():
    string_vector=[]
    mostrar_count=0
    with open(data_process_folder_superfile_header) as f:
        for line in f:
            time = line.split(";")[0]
            pseudotime = line.split(";")[1]
            dia,slot=divmod(int(pseudotime),1000)
            min = slot*3
            total_min=min+dia*24*60
            hora,min=divmod(min,60)
            if(mostrar_count%5==0):
                string_x=weekday[dia]+"_"+str(hora).zfill(2)+":"+str(min).zfill(2)
            else:
                string_x=""
            string_vector.append([total_min,string_x])
            mostrar_count+=1
    f.close()

    superfile= np.loadtxt(data_process_folder_superfile,delimiter=' ', dtype=np.dtype('int32'))

    #print superfile.shape[0]
    #print superfile.shape[1]
    diferential_matrix=np.zeros((superfile.shape[0], superfile.shape[1]))
    week_vector=[]
    y_matrix= np.empty((0,superfile.shape[1]), int)
    y_matrix_diferencia= np.empty((0,superfile.shape[1]), int)
    x_vector_value=[]
    x_vector_string=[]

    m=0
    n=0
    semana=1
    for i in range(0,superfile.shape[0]):
        x_vector_value.append(string_vector[i][0])
        x_vector_string.append(string_vector[i][1])
        y_matrix=np.vstack((y_matrix,np.empty((1,superfile.shape[1]), int)))
        y_matrix_diferencia=np.vstack((y_matrix_diferencia,np.empty((1,superfile.shape[1]), int)))
        #print "numpymatrix: "+str(y_matrix.shape[0])+": "+str(y_matrix.shape[1])

        n=0
        for j in range(0,superfile.shape[1]):
            #print "m :"+str(m)+" n: "+str(n)+" i: "+str(i)+" j: "+str(j)

            if(i==0):
                diferential_matrix[i,j]=0
            else:
                diferential_matrix[i,j]=superfile[i,j]-superfile[i-1,j]

            y_matrix[m,n]=superfile[i,j]
            y_matrix_diferencia[m,n]=diferential_matrix[i,j]
            n+=1

        m+=1
        if(string_vector[i][0]==10077):
            m=0
            week_vector.append([[x_vector_value,x_vector_string],y_matrix,y_matrix_diferencia])
            #print y_matrix_diferencia
            #print week_vector[len(week_vector)-1][2]
            y_matrix= np.empty((0,superfile.shape[1]), int)
            y_matrix_diferencia= np.empty((0,superfile.shape[1]), int)
            x_vector_value=[]
            x_vector_string=[]

            #print "Semana numero: "+str(semana)
            semana+=1

    #print week_vector
    #print "numero de semanas "+str(len(week_vector))

    #make plots
    # Auto-run Pycharm/python to Spark
    import matplotlib.pyplot as plt

    print "empezando hacer graficas"
    plt.close("all")

    plt.rc('xtick', labelsize=6)

    #print "plot primera semana"
    semana=0
    estacion=0
    for estacion in range(0,50):
        print "GRafica: "+str(estacion)
        fig,axarr=plt.subplots(2, sharex=True)
        fig.set_size_inches(90, 15)
        fig.suptitle('Station '+str(estacion), fontsize=22, fontweight='bold')
        axarr[0].set_title('Bikes')
        axarr[1].set_title('Delta Bikes')

        #len(week_vector)/3
        for semana in range(0,4):
            vector_x=week_vector[semana][0][0]
            vector_string_x=week_vector[semana][0][1]
            vector_y=week_vector[semana][1][:,estacion]
            vector_y_derivate=week_vector[semana][2][:,estacion]

            plt.xticks(vector_x, vector_string_x, rotation='vertical')
            axarr[0].set_xticklabels(vector_string_x)
            axarr[0].plot(vector_x,vector_y_derivate)
            axarr[1].plot(vector_x,vector_y)

        fig.savefig(data_process_folder_plots+str(estacion)+'.jpg',dpi = 100)
        plt.close("all")
    #plt.show()


    # fig=plt.figure()
    # fig.set_size_inches(25, 8)
    # fig.suptitle('Delta Bykes byStation '+str(estacion), fontsize=22, fontweight='bold')
    # for semana in range(0,len(week_vector)):
    #     vector_x=week_vector[semana][0][0]
    #     vector_string_x=week_vector[semana][0][1]
    #     vector_y_derivate=week_vector[semana][2][:,estacion]
    #     print "Semana: "+str(semana)
    #     print week_vector[semana][2]
    #
    #     plt.xticks(vector_x, vector_string_x, rotation='vertical')
    #     plt.plot(vector_x,vector_y_derivate)
    #
    # fig.savefig('test2.jpg',dpi = 100)
    # plt.show()


    np.savetxt(data_process_folder_superfile_diferential, diferential_matrix, delimiter=' ',newline='\n',fmt='%i')