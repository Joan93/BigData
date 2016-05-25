import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
m = Basemap(
        projection='merc',
        # llcrnrlon=0.031819,  # lower-left corner longitude
        # llcrnrlat=39.334322,  # lower-left corner latitude
        # urcrnrlon=4.240496,  # upper-right corner longitude
        # urcrnrlat=43.496240,  # upper-right corner latitude
        llcrnrlon=2.031819,  # lower-left corner longitude
        llcrnrlat=41.334322,  # lower-left corner latitude
        urcrnrlon=2.240496,  # upper-right corner longitude
        urcrnrlat=41.496240,  # upper-right corner latitude
        lat_ts=0,
        resolution='f',
        suppress_ticks=True)

# position in decimal lat/lon
lats=[41.4,41.45,41.49,41.36]
lons=[2.04,2.12,2.20,2.18]

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