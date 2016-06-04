# Ana Cristina Hernandez Gomez

#***************************************************************************************
# Para dibujar los edges hay que quitar el comentario en:
# linea: 75, 76, 86, 87

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap as Basemap
import Core.IdDictionary as IdDictionary

def run_main():
    [superdict,superlista] = IdDictionary.run_main()

    stations = np.genfromtxt("/home/ns3/Documents/BicingProject/BigData/Process_Data/Prematrix_data.txt",
                             delimiter=';',
                             dtype=[('lat', np.float32), ('lon', np.float32),('id', np.int16)],
                             usecols=(3, 4,0))

    ocupation = np.genfromtxt("/home/ns3/Documents/BicingProject/BigData/Process_Data/Data_history/1458255793_4001.txt",
                             delimiter=' ',
                             dtype=[('ocupacionabsoluta', np.float32), ('status', np.float32)],
                             usecols=(1, 2))

    m = Basemap(llcrnrlon=2.031819,llcrnrlat=41.334322,urcrnrlon=2.240496,urcrnrlat=41.496240, resolution = 'l',epsg=5520)
    #http://server.arcgisonline.com/arcgis/rest/services
    m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)

    lats=stations['lat']
    lons=stations['lon']
    ids=stations['id']
    OcupacionAbsoluta=ocupation['ocupacionabsoluta']
    Status=ocupation['status']
    OcupacionPorcentual=[]

    # convert lat and lon to map projection
    mx,my=m(lons,lats)

    pos={}
    counter=0
    for element in ids:
        pos[element]=(mx[counter],my[counter])
        if int(superdict[str(element)]['total'])==0:
            OcupacionPorcentual.append(100)
            print superdict[str(element)]['id']
        else:
            OcupacionPorcentual.append(int(round((float(OcupacionAbsoluta[counter])/float(superdict[str(element)]['total']))*100)))
        counter=counter+1

    print "/n"
    print OcupacionPorcentual

    Tuple = ()
    ListOfEdges = []

    ContadorFilas = 0
    ContadorColumnas = 0

    G = nx.Graph()

    # with open("/home/ns3/Documents/BicingProject/BigData/Process_Data/RDD/TrafficMatrix_data_python.txt","r") as fid:
    with open("/home/ns3/Documents/BicingProject/BigData/Process_Data/AdjacentMatrix.dat", "r") as fid:

        for line in fid:
            ContadorColumnas = 0
            f = line.split(' ')
            Tamano = len(f)
            for element in f:
                Tuple = str(ContadorFilas) + str(ContadorColumnas)
                if element == "1":
                    index1 = ids[ContadorFilas]
                    index2 = ids[ContadorColumnas]
                    #ListOfEdges.append((index1, index2))
                    #ListOfEdges.append((index1, index2))

                index1 = ids[ContadorFilas]
                index2 = ids[ContadorColumnas]
                G.add_node(index1)
                G.add_node(index2)

                ContadorColumnas = ContadorColumnas + 1
            ContadorFilas = ContadorFilas + 1

    #for EdgePair in ListOfEdges:
        #G.add_edge(EdgePair[0], EdgePair[1])

    color = []

    #min_altura = float(min(altura))
    #max_altura = float(max(altura))

    #step = (max_altura - min_altura) / 5

    #rango0 = min_altura
    #rango1 = min_altura + step * 1
    #rango2 = min_altura + step * 2
    #rango3 = min_altura + step * 3
    #rango4 = min_altura + step * 4
    #rango5 = max_altura

    # print min_altura
    # print max_altura
    # print step
    # print "/n"
    # print rango0
    # print rango1
    # print rango2
    # print rango3
    # print rango4
    # print rango5

    # Mientras el valor sea  mas pequeno, sera mas morado.
    # Mientras el valor de altura sea mas alto, sera mas rojo
    counter=0
    for element in OcupacionPorcentual:

        color.append(OcupacionPorcentual[counter])
        # if element >= rango0 and element < rango1:
        #     color.append(10)
        # if element >= rango1 and element < rango2:
        #     color.append(30)
        # if element >= rango2 and element < rango3:
        #     color.append(50)
        # if element >= rango3 and element < rango4:
        #     color.append(70)
        # if element >= rango4 and element <= rango5:
        #     color.append(90)
        counter=counter+1


    print color

    nx.draw_networkx(G, pos, node_size=150, node_color=color)
    plt.title('Bicing network classified according to occupation')
    plt.colorbar()
    plt.show()


