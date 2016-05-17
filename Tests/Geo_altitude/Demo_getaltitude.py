
import geocoder


g = geocoder.google('Mountain View, CA')
print g.latlng

g = geocoder.elevation([float(41.387953),float(2.150169)])
print (g.meters)

