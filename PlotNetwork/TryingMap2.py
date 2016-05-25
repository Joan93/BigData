import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

airports = np.genfromtxt("/home/ns3/Documents/BicingProject/BigData/Process_Data/RDD/Prematrix_data_python.txt",
                         delimiter=';',
                         dtype=[('lat', np.float32), ('lon', np.float32)],
                         usecols=(3, 4))

themap = Basemap(projection='gall',
                 llcrnrlon=2.031819,  # lower-left corner longitude
                 llcrnrlat=41.334322,  # lower-left corner latitude
                 urcrnrlon=2.240496,  # upper-right corner longitude
                 urcrnrlat=41.496240,  # upper-right corner latitude
                 resolution='f',
                 area_thresh=1000.0,
                 )

themap.drawcoastlines()
themap.drawcountries()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')

x, y = themap(airports['lon'], airports['lat'])
#c=airports['alt']
#themap.pcolor(x,y,)
themap.plot(x, y,
            'o',                    # marker shape
            color='coral',         # marker colour
            markersize=4            # marker size
            )

plt.show()