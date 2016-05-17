#matplotlib inline  # In ipython or ipython notebook only
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# Define the projection, scale, the corners of the map, and the resolution.
m = Basemap(projection='merc',llcrnrlat=41,urcrnrlat=42,\
            llcrnrlon=2,urcrnrlon=3,resolution='f')
# Draw the coastlines
m.drawcoastlines()
# Color the continents
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
#m.drawparallels(np.arange(-90.,91.,30.))
#m.drawmeridians(np.arange(-180.,181.,60.))
# fill in the oceans
m.drawmapboundary(fill_color='aqua')
plt.title("Mercator Projection")
plt.show()
