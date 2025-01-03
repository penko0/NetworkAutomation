list1 = ['Cisco', 'arista', 'juniper']

#Prints all elements with small letters 
# for vendor in list1:
#     print(f"Vendor name is: {vendor.casefold()}")

# for n in range(1,10):
#     print(f"10.1.1.{n}")

# n = 0 
# for i in range(1,10):
#     n += i
#     print(f"i is {i}, n is {n}")

d1 = {'ip': '1.1.1.1', 'username':'admin', 'password':'pwd123'}
# for i in d1:
#     print(i)     #Prints the keys of the dictionary   
#     print(d1[i]) #Prints the values

# for i in d1.values():
#     print(i)

# for i in d1.keys():
#     print(i)

#To print key:value pairs in a tuple:

# for i in d1.items():
#     print(i)

# for i in d1.items():
#     print(f"The key is: {i[0]}") #Print the keys
#     print(f"The value is: {i[1]}\n") #Print the values of our keys

# for k,v in d1.items():
#     print(f"The key is: {k}\nThe value is {v}") #Print the keys
    

# '''for else'''
# for i in list1:
#     if i == 'aritsa':
#         break
#     print(i)
# else:
#     print("Iteration completed")
# print("Completed")

#Example with continue
for i in list1:
    if i == 'arista':
        continue
    print(i)
else:
    print("Iteration completed")
print("Completed")


'''Nested Loop'''
ips = ['192.168.1.1','192.168.1.2','192.168.1.3']
confs = ['conf t','int gi 1']

for ip in ips:
    print(f"Configuration for {ip} is:")
    for conf in confs:
        print(conf.rjust(20))

'''pass'''
# for i in list1:
#     pass