###### enumerate()

vendors = ['cisco', 'arista', 'juniper', 'HP', 'extreme']
print(vendors.index('cisco')) #prints the index
print(vendors[0])

e = enumerate(vendors)
print(e)

#Here we print indexes with their values
for index in e:
    print(index)

''' If we want to change the initial index(default is 0)'''
for index in enumerate(vendors, start=10):  
    print(index)


#If we do not want to print a tuple
for index, name in enumerate(vendors):  
    print(index,name)

users = ['user1', 'user2', 'user3', 'user4']
search = input("Enter Username: ")
for index, name in enumerate(users):
    if name == search:
        print(f"User {search} index is {index}")
        break
else:
    print("Not found")