"""
####################
Python      Json
--------------------
dict	    object
list,tuple	array
str	        string
int,float	number
True	    true
False	    false
None	    null
###################
      dump
Python >>> JSON
Python <<< JSON
      load
###################
"""
import json
from lab_inventory import *

## dump : directly saves to a file as json data
# with open('inventory_list.json', 'w') as data:
#     json.dump(inventory_list, data, indent=4)

# # From Python to JSON dictionary format 
# with open('inventory_list_of_dict.json', 'w') as data:
#     json.dump(inventory_list_of_dict, data, indent=4)

# with open('inventory_dict.json', 'w') as data:
#     json.dump(inventory_dict, data, indent=4)

## dumpS : converts Python list to json  string
with open('lab_data.json', 'w') as data:
    st = json.dumps(inventory_list, indent=4)
    data.write(st)
print(st)
print(type(st))


## loaD : reads directly from file: converts JSON data to python format
# with open('lab_data.json') as file:
#     output = json.load(file)
# print(output)
# print(type(file))



## loadS: converts JSON string to python format
with open('lab_data.json') as file:
    json_data = file.read()
print(json_data)
print(type(json_data))

#Here the end result is Python list
output = json.loads(json_data)
print(output)
print(type(output))