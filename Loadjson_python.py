import json

from pprint import pprint

with open('Data/data.json') as data_file:
    data = json.load(data_file)

#print data["updateTime"]
time=data["updateTime"]

print ('Uptade Time: %i' %time)

#pprint(data)
#print data["stations"]
#station


for i in xrange(10):
    #print ('Uptade Time: %i' %print data["stations"][i]["id"])
    print data["stations"][i]["id"]
    print data["stations"][i]["altitude"]
    print data["stations"][i]["longitude"]
    print data["stations"][i]["latitude"]
    print data["stations"][i]["bikes"]
    print data["stations"][i]["slots"]
    print data["stations"][i]["type"]
    print data["stations"][i]["status"]


#for data[""]

f = open("Process_Data/data_python.txt", 'w+')

for i in xrange(len(data)):

    f.write(data["stations"][i]["id"])
    f.write(" ")
    f.write(data["stations"][i]["altitude"])
    f.write(" ")

    f.write(data["stations"][i]["latitude"])
    f.write(" ")
    f.write(data["stations"][i]["bikes"])
    f.write(" ")


    f.write(data["stations"][i]["slots"])
    f.write(" ")
    f.write(data["stations"][i]["type"])
    f.write(" ")


    f.write(data["stations"][i]["status"]+"\n")