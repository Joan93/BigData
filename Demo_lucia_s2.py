import numpy as np
from collections import OrderedDict
import os

alturas=np.array([[0,10,60,5],[10,0,8,6],[60,8,0,4],[5,6,4,0]],dtype='f')
distancias=np.array([[0,100,2400,500],[100,0,2000,600],[2400,2000,0,800],[500,600,800,0]],dtype='f')

print alturas
print "\n"
print distancias
print "\n"
np.seterr(divide='ignore', invalid='ignore')
inclination= np.divide(alturas, distancias)
print inclination
print "\n"
inclination[inclination == np.inf] = 0
inclination2 = np.nan_to_num(inclination)

print inclination2