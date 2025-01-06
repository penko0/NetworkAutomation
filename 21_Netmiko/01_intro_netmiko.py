from netmiko import Netmiko

## Netmiko
csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}

net_connect = Netmiko(**csr)
print("Connected successfully")
# print(dir(net_connect)) #Available methots for Netmiko

#Shows running config
sh_output = net_connect.send_command('show run')
print(sh_output)

# print(net_connect.find_prompt())
print(net_connect.check_config_mode())
print(f"Is enable mode active?: {net_connect.check_enable_mode()}")

''' Enter config mode (configure terminal) '''
net_connect.config_mode()
print(f"Is config mode active?: {net_connect.check_config_mode()}")
print(net_connect.find_prompt())
