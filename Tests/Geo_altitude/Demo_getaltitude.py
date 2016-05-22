
import geocoder


g = geocoder.google('Mountain View, CA')
print g.latlng

g = geocoder.elevation([float(41.387953),float(2.150169)])
print (g.meters)

g = geocoder.google([45.15, -75.14], method='elevation')
print g.meters