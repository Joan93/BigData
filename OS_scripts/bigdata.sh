# Super script de bigdata Rodrigo UPC-MASTEAM Bigdata
# This script collect the data of Barcelona Bicing API each 3 min through crontab
#!/bin/bash 

fecha="$(date +"%m-%d-%Y_%H_%M")"
wget http://wservice.viabicing.cat/v2/stations -O ~/bigdata2/$fecha.json

#processing data
#update stadistics
