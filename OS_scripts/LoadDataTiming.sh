#This script run spark and python version to process json files storage
# and timing to select the best option
#!/bin/bash
spark_path="/home/rodrigo/PycharmProjects/BigData/Loadjson_to_RDD.py"
python_path="/home/rodrigo/PycharmProjects/BigData/Loadjson_python.py"

(time python $spark_path ) 2> timing1.txt
(time python python_path ) 2> timing2.txt