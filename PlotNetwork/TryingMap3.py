import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
m = Basemap(
        projection='merc',
        llcrnrlon=-130,
        llcrnrlat=25,
        urcrnrlon=-60,
        urcrnrlat=50,
        lat_ts=0,
        resolution='i',
        suppress_ticks=True)

# position in decimal lat/lon
lats=[37.96,42.82,39,49]
lons=[-121.29,-73.95,-82,-100]

# convert lat and lon to map projection
mx,my=m(lons,lats)

# The NetworkX part
# put map projection coordinates in pos dictionary
G=nx.Graph()
G.add_edge('a','b')
G.add_edge('a','c')
G.add_node('d')

pos={}
pos['a']=(mx[0],my[0])
pos['b']=(mx[1],my[1])
pos['c']=(mx[2],my[2])
pos['d']=(mx[3],my[3])
# draw
nx.draw_networkx(G,pos,node_size=200,node_color='blue')


# Now draw the map
m.drawcountries()
m.drawstates()
m.bluemarble()
plt.title('How to get from point a to point b')
plt.show()