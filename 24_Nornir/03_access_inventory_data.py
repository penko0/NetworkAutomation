from nornir import InitNornir

nr = InitNornir(config_file="config.yaml") #Config file in YAML format

print(nr.inventory)
print(nr.inventory.hosts)
print(nr.inventory.groups)
print(nr.inventory.defaults)
print(f" Username: {nr.inventory.defaults.username}")
print(f" Username: {nr.inventory.defaults.password}")

all_hosts = nr.inventory.hosts
for host in all_hosts:
    print(f"Hostname: {host}")

r1_host = nr.inventory.hosts['rtr1']
print(type(r1_host))
print(dir(r1_host))
#We can print particular value from our YAML configuration
print(r1_host.platform)
print(r1_host.data)
print(r1_host['site'])

cisco_grp = nr.inventory.groups['cisco_group']
print(f"The platform is: {cisco_grp.platform}")