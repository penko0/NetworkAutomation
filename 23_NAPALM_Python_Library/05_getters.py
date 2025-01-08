from napalm import get_network_driver
from pprint import pprint

driver = get_network_driver('ios')
device = driver(hostname='192.168.1.23', username='admin', password='admin')
device.open()
print("Connected successfully")
# pprint(device.get_facts()['interface_list'])
# pprint(device.get_config())
# pprint(device.get_interfaces())
# pprint(device.get_interfaces_ip())
# pprint(device.get_environment())
pprint(device.ping('192.168.1.1'))
device.close()
print("Done")