import json

from pprint import pprint

with open('Data/data.json') as data_file:
    data = json.load(data_file)

print data["updateTime"]

print ('Uptade Time: %f' %data["updateTime"])



#pprint(data)

#print data["stations"]



for i in xrange(10):
    print data["stations"][i]["id"]
    print data["stations"][i]["altitude"]
    print data["stations"][i]["longitude"]
    print data["stations"][i]["latitude"]
    print data["stations"][i]["bikes"]
    print data["stations"][i]["slots"]
    print data["stations"][i]["type"]
    print data["stations"][i]["status"]


#for data[""]

