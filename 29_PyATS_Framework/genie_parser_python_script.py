from genie.testbed import load
from pprint import pprint
from tabulate import tabulate
tb = load('yaml/my_testbed.yaml')
dev = tb.devices["CSR3"]

dev.connect(log_stdout=False) # This will not print stdout to our terminal

show_version_parsed = dev.parse("show version")
show_ip_int_br_parsed = dev.parse("show ip interface brief")

''' Creates a dictionary with interface data'''
int_parsed = show_ip_int_br_parsed['interface']



print(show_version_parsed, "\n")
print(show_ip_int_br_parsed, "\n")

# print(tabulate(show_ip_int_br_parsed)) #Just for tests , what will be printed on the screen

''' Prints given interface from the dictionary that we created earlier'''
# print(show_ip_int_br_parsed['interface']['GigabitEthernet2'])
print(show_version_parsed['version']['chassis'])

# pprint(dir(dev.api)) # Print all the methods that we can use

print(int_parsed)
for int in int_parsed:
    print(int)


for int in int_parsed:
    print(f"NAME: {int}, IP: {int_parsed[int]['ip_address']}")