#With exceptions, we see the error for particular device and continue script executionwith for rest of the devices

from netmiko import ConnectHandler, exceptions


csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}
vIOS1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.172',
    'username': 'admin',
    'password': 'adminn'
}
vISR = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.25',
    'username': 'admin',
    'password': 'admin'
}

device_list = [csr, vIOS1, vISR]
for device in device_list:
    try:
        print(f"\n{'#' * 35}\nConnecting to device {device['host']}")
        net_connect = ConnectHandler(**device)
        print(f"Connected successfully to device {device['host']} ")
        print(net_connect.find_prompt())
        print(net_connect.send_command("show ip int brie"))
        net_connect.disconnect()
    except exceptions.NetmikoAuthenticationException:
        print(f"Authentication Failed on {device['host']}")
    except exceptions.NetmikoTimeoutException:
        print(f"Session timeout on {device['host']}")