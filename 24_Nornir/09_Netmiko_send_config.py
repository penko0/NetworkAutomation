#For this task we import netmiko_send_config

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_config


nr = InitNornir(config_file="config.yaml") #Config file in YAML format
ios = nr.filter(platform='ios')

print_title("Nornir Netmiko send config")

commands = ['ip route 1.1.1.1 255.255.255.255 192.168.1.1',
            'no ip route 1.1.1.2 255.255.255.255 192.168.1.1']
#Here we use list of commands
#get_results = ios.run(task=netmiko_send_config, config_commands=commands)


#Here we use config file to add/remove the static routes
get_results = ios.run(task=netmiko_send_config, config_file="add_routes.txt")


#Print results
print_result(get_results)