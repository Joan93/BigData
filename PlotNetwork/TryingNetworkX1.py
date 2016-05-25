#################################################################################################
#                                                                                               #
#                       Script para plotear las estaciones                                      #
#                                                                                               #
#################################################################################################

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#El archivo es: TrafficMatrix_data_python
#BaseMap de Matplotlib

#G = nx.gnp_random_graph(10,0.02)

NumberOfStations=496
Matrix=np.zeros((NumberOfStations,NumberOfStations))
Status=np.zeros((NumberOfStations,2))

G=nx.Graph()
G.add_node(NumberOfStations)

#H=nx.path_graph(10)
#G.add_nodes_from(H)#G.add_edges_from

Tuple=()
ListOfEdges =[]

ContadorFilas=0
ContadorColumnas=0
with open("/home/ns3/Documents/BicingProject/BigData/Process_Data/RDD/TrafficMatrix_data_python_BIG.txt","r") as fid:
    for line in fid:
        ContadorColumnas=0
        f=line.split(' ')
        for element in f:
            Tuple= str(ContadorFilas) + str(ContadorColumnas)
            Matrix[ContadorFilas, ContadorColumnas] = element
            if element=="1":
                print "(" + str(ContadorFilas) + "," + str(ContadorColumnas) + ")"
                ListOfEdges.append((ContadorFilas+1,ContadorColumnas+1))

            G.add_node(ContadorFilas+1)
            G.add_node(ContadorColumnas+1)

            ContadorColumnas=ContadorColumnas+1
        ContadorFilas=ContadorFilas+1

for EdgePair in ListOfEdges:
    #print EdgePair[0]
    G.add_edge(EdgePair[0],EdgePair[1])

#G.add_node([1,10])
#G.add_edges_from(ListOfEdges())
#G=nx.Graph(ListOfEdges)

print G.nodes()
print G.edges()
nx.draw(G)
plt.savefig("/home/ns3/Documents/BicingProject/BigData/PlotNetwork/degree_histogram.png")
#nx.draw_circular(G)
#nx.draw_spectral(G)

plt.show()

print Matrix
print ListOfEdges


