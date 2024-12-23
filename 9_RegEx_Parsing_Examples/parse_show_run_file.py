import re
from pprint import pprint
hostname_pattern = re.compile(r'hostname (\S+)')
domain_name_pattern = re.compile(r'ip domain name(.+)')
pid_pattern = re.compile(r'license udi pid (\w+) sn (\S+)')
netconf_pattern = re.compile(r'netconf-yang\n')
username_pattern = re.compile(r'username (\S+) privilege (\d{1,2})')
#This finds interface name ,address and mask
interface_pattern = re.compile(r'interface (\S+)(\n.+?)+\n?\s?ip address ([\d\.]+) ([\d\.]+)') # www.regex101.com
#This finds the properties of interface(ip, netmask ...)
interface_prop_pattern = re.compile(r'interface (?P<name>\S+)(\n.+?)+\n?\s?ip address (?P<ip_address>[\d\.]+) (?P<netmask>[\d\.]+)')

with open('show_running-config.txt') as file:
    output = file.read()
    hostname_match = hostname_pattern.search(output)
    print('Hostname is:'.ljust(18) + str(hostname_match.group(1)))
    domain_name_match = domain_name_pattern.search(output)
    print('Domain name is:'.ljust(18) + str(domain_name_match.group(1)))
    pid_match = pid_pattern.search(output)
    print('The PID is:'.ljust(18) + str(pid_match.group(1)))
    print('SN is:'.ljust(18) + str(pid_match.group(2)))

    netconf_match = netconf_pattern.search(output)
    if netconf_match:
        print('Netconf Enabled:'.ljust(18) + 'Yes')
        print(netconf_match)
    else:
        print('Netconf is not enabled')

    username_iter = username_pattern.finditer(output)
    user_list = []
    print(username_iter)
    for user in username_iter:
        print(user.group(1))
        user_list.append(user.group(1))
    print('User list:'.ljust(18) + str(user_list))


interface_iter = interface_pattern.finditer(output) #When we have multiple values , we use finditer() method 

interface_list = []
for interface in interface_iter:
    print(interface.group(1))
    interface_list.append(interface.group(1))
print('Interfaces with IP address:'.ljust(18) + str(interface_list))

interface_prop = interface_prop_pattern.finditer(output)
interface_properties_list = list()

for interface_conf in interface_prop:
    interface_properties_list.append(interface_conf.groupdict())
print(interface_properties_list)
pprint(interface_properties_list, indent=5)