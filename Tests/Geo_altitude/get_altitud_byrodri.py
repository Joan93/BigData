import requests


url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Mountain View, CA'}
r = requests.get(url, params=params)
print r
results = r.json()['results']
location = results[0]['geometry']['location']

print (location['lat'])
print (location['lng'])