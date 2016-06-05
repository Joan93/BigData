# Ana Cristina Hernandez Gomez

# cargo latitudes y longitudes cargadas para plotear el mapa
# cargo la informacion de ocupacion de todas las estaciones en un determinado momento del dia
# cargo la informacion de peso para cada enlace (a traves de la matriz de pesos)
# cargo la matriz de adjacencia para poder determinar las conexiones.

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

    weights = np.genfromtxt("/home/ns3/Documents/BicingProject/BigData/Process_Data/WeightMatrix_300.dat",
                              delimiter=' ')
    print weights[1,2]

    m = Basemap(llcrnrlon=2.031819,llcrnrlat=41.334322,urcrnrlon=2.240496,urcrnrlat=41.496240, resolution = 'l',epsg=5520)
    #http://server.arcgisonline.com/arcgis/rest/services
    m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)

    lats=stations['lat']
    lons=stations['lon']
    ids=stations['id']


    # convert lat and lon to map projection
    mx,my=m(lons,lats)

    pos={}
    counter=0
    for element in ids:
        pos[element]=(mx[counter],my[counter])
        counter=counter+1

    #print "/n"
    #print OcupacionPorcentual

    Tuple = ()
    ListOfEdges = []
    ListOfWeights=[]

    ContadorFilas = 0
    ContadorColumnas = 0

    G = nx.Graph()


    # with open("/home/ns3/Documents/BicingProject/BigData/Process_Data/RDD/TrafficMatrix_data_python.txt","r") as fid:
    with open("/home/ns3/Documents/BicingProject/BigData/Process_Data/AdjacentMatrix_distance_300.dat", "r") as fid:

        for line in fid:
            ContadorColumnas = 0
            f = line.split(' ')
            Tamano = len(f)
            for element in f:
                Tuple = str(ContadorFilas) + str(ContadorColumnas)
                if element == "1":
                    index1 = ids[ContadorFilas]
                    index2 = ids[ContadorColumnas]
                    weight=weights[ContadorFilas,ContadorColumnas]
                    if weight >= 0 and weight < 100:
                        colors = 10
                    if weight >= 100 and weight < 200:
                        colors = 20
                    if weight >= 200 and weight < 300:
                        colors = 30
                    if weight >= 300 and weight < 400:
                        colors = 40
                    if weight >= 400 and weight <= 500:
                        colors = 50
                    if weight >= 500 and weight < 600:
                        colors = 60
                    if weight >= 600 and weight < 700:
                        colors = 70
                    if weight >= 700 and weight < 800:
                        colors = 80
                    if weight >= 800 and weight < 900:
                        colors = 90
                    if weight >= 900 and weight < 1000:
                        colors = 100
                    if weight>=1000:
                        colors=0
                    ListOfWeights.append((colors))
                    ListOfEdges.append((index1, index2,colors))
                    ListOfWeights.append((colors))
                    ListOfEdges.append((index1, index2,colors))


                index1 = ids[ContadorFilas]
                index2 = ids[ContadorColumnas]
                G.add_node(index1)
                G.add_node(index2)

                ContadorColumnas = ContadorColumnas + 1
            ContadorFilas = ContadorFilas + 1


    print len(ListOfEdges), len(ListOfWeights)

    for EdgePair in ListOfEdges:
        G.add_edge(EdgePair[0], EdgePair[1],color=EdgePair[2])



    #nx.draw_networkx(G, pos, node_size=150,edge_color=ListOfWeights)
    edges = G.edges()
    colores = [G[u][v]['color'] for u, v in edges]
    nx.draw(G, pos, edges=edges, edge_color=colores, node_color='blue',node_size=100,font_size=8)
    #nx.draw(G,pos,edge_color=ListOfWeights)
    plt.title('Bicing network - Weighted links')
    plt.colorbar()
    plt.show()


