from netmiko import ConnectHandler, exceptions
from datetime import datetime
import threading

lab_csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}
vISR = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.25',
    'username': 'admin',
    'password': 'admin'
}
vIOS2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.172',
    'username': 'admin',
    'password': 'admin'
}
hosts = [lab_csr, vISR, vIOS2]
start_time = datetime.now()

def netmiko_connect(**device):
    try:
        net_connect = ConnectHandler(**device)
        print(f"Connected Successfully to device: {device['host']}")
        output = net_connect.send_command('show version')
        # print(output)
        print(f"Writing output to the File: {device['host']}.txt")
        with open(f"{device['host']}.txt", 'w') as data:
            data.write(output)
        net_connect.disconnect()
    except exceptions.NetmikoAuthenticationException:
        print(f"Authentication failed on {device['host']}")
    except exceptions.NetmikoTimeoutException:
        print(f"Session timeout on {device['host']}")

# netmiko_connect(**vISR)
# netmiko_connect(**vIOS2)
# netmiko_connect(**lab_csr)
# end_time = datetime.now()
# print(end_time - start_time)


''' Threading variant that is FASTER for execution'''
cisco_config_threads = []
for host in hosts:
    config_thread = threading.Thread(target=netmiko_connect, kwargs=host)
    config_thread.start()
    cisco_config_threads.append(config_thread)
for thread in cisco_config_threads:
    thread.join()

end_time = datetime.now()
print(end_time - start_time)