#For this task we import netmiko_send_command

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yaml") #Config file in YAML format
ios = nr.filter(platform='ios')

print_title("Nornir Netmiko send command")

get_results = ios.run(task=netmiko_send_command, command_string="show version")
#Print results
print_result(get_results)