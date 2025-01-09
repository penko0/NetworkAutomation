from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get


nr = InitNornir(config_file="config.yaml") #Config file in YAML format
# nr = InitNornir() #Here nornir looks for default config file hosts.yaml

'''Prints only routers located in site IND'''
# print(nr.filter(site='IND').inventory.hosts.keys())
site_ind = nr.filter(site='IND')
dc_blr = nr.filter(dc='BLR')
rtr1 = nr.filter(name='rtr1')
ios = nr.filter(platform='ios')
# print(type(site_ind))
# print(dir(site_ind))

#Declate the filter in "results
# results = nr.run(task=napalm_get, getters=['facts', 'interfaces'])
# results = site_ind.run(task=napalm_get, getters=['facts', 'interfaces'])
# results = dc_blr.run(task=napalm_get, getters=['facts', 'interfaces'])
# results = rtr1.run(task=napalm_get, getters=['facts', 'interfaces'])
results = ios.run(task=napalm_get, getters=['facts', 'interfaces'])
print_result(results)

