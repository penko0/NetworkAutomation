from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from datetime import datetime
# nr = InitNornir(config_file="config.yaml") #Config file in YAML format
start_time = datetime.now()
nr = InitNornir() #Here nornir looks for default config file hosts.yaml
results = nr.run(task=napalm_get, getters=['facts', 'interfaces'])

print_result(results)
end_time = datetime.now()
print(end_time - start_time)