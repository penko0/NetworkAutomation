device_info_list = [
    ['name', 'router'],
    ['vendor', 'cisco'],
    ['model', 'vIOS'],
    ['ip', '1.1.1.1']
]
device_info = [
    ('name', 'router'),
    ('vendor', 'cisco'),
    ('model', 'vIOS'),
    ('ip', '1.1.1.1')
]



device_dict = dict()

for device in device_info_list:
    device_dict[device[0]] = device[1]

print(device_dict)


device_dict_new = { device[0]:device[1] for device in device_info_list }
print(device_dict_new)
print(device_dict_new.items())

#Will print a tuple
# for i in device_dict_new.items():
#     print(i)

# for key, value in device_dict_new.items():
#     print(key, value)


#How to create a dictionary from string 
device_str = 'name:router, vendor:cisco, model:vIOS, ip: 1.1.1.1'
device_list = device_str.split(',') #This splits the string depending on the "," sign.
print(device_list)

device_dict_new = dict()

for item in device_list:
    device_list
    k = item.split(':')
    print(k)
    device_dict_new[k[0].strip()] = k[1].strip() #Mapping key: value pairs and removing whitespaces
print(device_dict_new)

# device_dict = {item.split(":")[0].strip():item.split(":")[1].strip() for item in device_str.split(',')}
# print(device_dict)
