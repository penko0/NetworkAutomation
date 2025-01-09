#For this task we import napalm_configure
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_configure

nr = InitNornir(config_file="config.yaml") #Config file in YAML format
ios = nr.filter(platform='ios')


print_title("NAPALM Configure TASK")
#Here we use commands to config devices
# conf_results = ios.run(task=napalm_configure, configuration="no interface loopback 1005")

#Here we use config file to configure our routers/devices with static routes
# conf_results = ios.run(task=napalm_configure, filename='add_routes.txt')
#Remove static routes
conf_results = ios.run(task=napalm_configure, filename='remove_routes.txt')

print_result(conf_results)

print_title("NAPALM CLI TASK")
cli_results = ios.run(task=napalm_cli, commands=['show run | in ip route'])
print_result(cli_results)
