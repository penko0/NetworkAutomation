#For this task we import napalm_cli
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli

'''''Here we print the title'''
print_title("NAPALM GET TASK")
nr = InitNornir(config_file="config.yaml") #Config file in YAML format
# nr = InitNornir() #Here nornir looks for default config file hosts.yaml

'''Define filter'''
ios = nr.filter(platform='ios')

get_results = ios.run(task=napalm_get, getters=['facts', 'interfaces_ip'])
#Print results
print_result(get_results)

print_title("NAPALM CLI TASK")
cli_results = ios.run(task=napalm_cli, commands=['show version', 'show ip interface brief'])
# print_result(cli_results)

#Here we receive the output in string format
print(cli_results['rtr1'].result['show version'])