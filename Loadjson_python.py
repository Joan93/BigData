import json

from pprint import pprint

with open('Data/data.json') as data_file:
    data = json.load(data_file)

print data["updateTime"]

#pprint(data)

print data["stations"]
