
import geocoder


g = geocoder.google('Mountain View, CA')
print g.latlng


g = geocoder.elevation([41.397952,2.180042])
print (g.meters)

g = geocoder.google([41.397952,2.180042], method='elevation')

print (g.meters)