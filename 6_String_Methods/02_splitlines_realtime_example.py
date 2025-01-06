show_output = '''GigabitEthernet0/0         192.168.1.172   YES NVRAM  up                    up      
GigabitEthernet0/1         unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/2         unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/3         unassigned      YES NVRAM  administratively down down    
Loopback1                  4.4.4.4         YES manual up                    up    
'''
interfaces = show_output.splitlines()
#print(interfaces) #prints a list

for int in interfaces:
    print(int)
    
#If we want to print each interace`s properties as a list, do the following

for int in interfaces:
    print(int.split())

#If we want to display particular property/value from the output
for int in interfaces:
    int_details = int.split()
    if int_details[1] == 'unassigned':
        continue 
    print(f"Interface Name: {int_details[0]} Interface IP {int_details[1]}")


#How to print the content of config file
with open('csr_config.txt') as text: 
    lines = text.readlines() #First we convert the content to [list] . readlines() method does it.
    print(lines)
    for line in lines:
        print('\033[34m' + line, end='') # '\033[34m' adds blue color to the output , see the reference table in Internet