from netmiko import ConnectHandler, exceptions
import logging
logging.basicConfig(filename='ssh_log', level=logging.DEBUG)
lab_csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.23',
    'username': 'admin',
    'use_keys': True,
    'key_file': '/home/pen/.ssh/id_rsa',
    'disabled_algorithms': dict(pubkeys=['rsa-sha2-512', 'rsa-sha2-256'])
}

try:
    net_connect = ConnectHandler(**lab_csr)
    print("Connected Successfully")
    cmd_output = net_connect.send_command('show ip int brief')
    print(cmd_output)
    net_connect.disconnect()
except exceptions.NetmikoAuthenticationException:
    print(f"Authentication failed on {lab_csr['host']}")
except exceptions.NetmikoTimeoutException:
    print(f"Session timeout on {lab_csr['host']}")

