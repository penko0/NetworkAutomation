from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}

net_connect = Netmiko(**csr)
print("Connected successfully")