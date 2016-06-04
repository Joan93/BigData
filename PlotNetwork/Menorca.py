

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap

import Core.IdDictionary as IdDictionary

[superdict,superlista] = IdDictionary.run_main()
#a=superlista[5]['alt']
#b=superdict['496']['alt']
#print b

stations = np.genfromtxt("/home/ns3/Documents/BicingProject/BigData/Process_Data/RDD/Prematrix_data_python.txt",
                         delimiter=';',
                         dtype=[('lat', np.float32), ('lon', np.float32),('id', np.int16)],
                         usecols=(3, 4,0))

m = Basemap(llcrnrlon=2.031819,llcrnrlat=41.334322,urcrnrlon=2.240496,urcrnrlat=41.496240, resolution = 'l',epsg=5520)
#http://server.arcgisonline.com/arcgis/rest/services
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)

lats=stations['lat']
lons=stations['lon']
ids=stations['id']
altura=[]

# convert lat and lon to map projection
mx,my=m(lons,lats)

pos={}
counter=0
for element in ids:
    pos[element]=(mx[counter],my[counter])
    altura.append(float(superdict[str(element)]['alt']))
    counter=counter+1
# pos['a']=(mx[0],my[0])
# pos['b']=(mx[1],my[1])
# pos['c']=(mx[2],my[2])
# pos['d']=(mx[3],my[3])

print counter
print "aaaaaaaaaaa"
print altura

# print lats
#print ids[0]

Tuple=()
ListOfEdges =[]

ContadorFilas=0
ContadorColumnas=0

G=nx.Graph()

#with open("/home/ns3/Documents/BicingProject/BigData/Process_Data/RDD/TrafficMatrix_data_python.txt","r") as fid:
with open("/home/ns3/Documents/BicingProject/BigData/Process_Data/AdjacentMatrix.dat", "r") as fid:

    for line in fid:
        ContadorColumnas=0
        f=line.split(' ')
        Tamano=len(f)
        #print Tamano
        for element in f:
            Tuple= str(ContadorFilas) + str(ContadorColumnas)
            #Matrix[ContadorFilas, ContadorColumnas] = element
            if element=="1":
                #print "(" + str(ContadorFilas) + "," + str(ContadorColumnas) + ")"
                index1=ids[ContadorFilas]
                index2=ids[ContadorColumnas]
                ListOfEdges.append((index1, index2))
                ListOfEdges.append((index1,index2))

            index1 = ids[ContadorFilas]
            index2 = ids[ContadorColumnas]
            G.add_node(index1)
            G.add_node(index2)

            ContadorColumnas=ContadorColumnas+1
        ContadorFilas=ContadorFilas+1

for EdgePair in ListOfEdges:
    #print EdgePair[0]
    G.add_edge(EdgePair[0],EdgePair[1])


# lats=[41.4,41.45,41.49,41.36]
# lons=[2.04,2.12,2.20,2.18]


# The NetworkX part
# put map projection coordinates in pos dictionary


# G.add_edge('a','b')
# G.add_edge('a','c')
# G.add_node('d')
color=[]

min_altura=float(min(altura))
max_altura=float(max(altura))

step=(max_altura-min_altura)/5

rango0=min_altura
rango1=min_altura+step*1
rango2=min_altura+step*2
rango3=min_altura+step*3
rango4=min_altura+step*4
rango5=max_altura

#print min_altura
#print max_altura
#print step
#print "/n"
#print rango0
#print rango1
#print rango2
#print rango3
#print rango4
#print rango5

#Mientras el valor sea  mas pequeno, sera mas morado.
#Mientras el valor de altura sea mas alto, sera mas rojo
for element in altura:
    if element>=rango0 and element<rango1:
        color.append(10)
    if element>= rango1 and element<rango2:
        color.append(30)
    if element>=rango2 and element<rango3:
        color.append(50)
    if element>=rango3 and element<rango4:
        color.append(70)
    if element>=rango4 and element<=rango5:
        color.append(90)

#color=['blue','blue','blue','coral','blue','blue','blue','blue','blue','blue']
print color
# draw
nx.draw_networkx(G,pos,node_size=150,node_color=color)
# Now draw the map
#m.drawcountries()
#m.drawstates()
#m.bluemarble()
plt.title('Bicing network classified according to height')
plt.show()