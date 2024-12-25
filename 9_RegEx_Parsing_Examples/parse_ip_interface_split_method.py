from pprint import pprint

with open('show_ip_interface_brief.txt') as file:
    output = file.read()

# print(output) #Prints the text as one string
output_list = output.splitlines()
# print(output_list)

interface_list = output_list[2:]
print(interface_list)
for interface in interface_list:
    print(interface.split())
print('\n')

int_parsed_list = list()
for interface in interface_list:
    intf_dict = {}
    intf = interface.split()
    intf_dict['int_name'] = intf[0]
    intf_dict['int_IP'] = intf[1]
    intf_dict['int_status'] = intf[-2]
    int_parsed_list.append(intf_dict)
    print(intf_dict)
pprint(int_parsed_list)

for intf in int_parsed_list:
    if intf['int_status'] == 'down':
        print(intf)
