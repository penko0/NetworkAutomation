from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}



''' Commands in list format'''
commands = [f'int lo1001', f'ip address 11.1.1.10 255.255.255.0', 'no shut']


''' SSH key transfer does not work... like that Нещо май не става така ... '''
# ssh_key_part1 = '''ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDG+DsXZNki830AbyeccpBRQ4Kk
# nWKf84I2xUnpAWFA4WfQzirUf9uZPVnIZve5IIEFiN6CM4bjHNFxvl8DCyrDo5n7
# HOwSsKCmciXVKER5qV4VM2xCTARZLxfpU8BH0kDNeNiv0xgmmh79lYobf4cutwrm
# IVDOwDLzJcq2AyBX4uOM2GI9vlSIKypOceOD0XVQioooOXXZiu4iZzK2XAGeFESE
# hhVj6oFWwNH14EOOT3CbSpGVoysdZT08/Kwd3LHmI5Wu6xd9qGTAsUw3Amy81pnH
# ALJEnEAncN3i6oj9uNmTv3R+AShYhdYyiauokk3fVorbxegT8Iz4avJu09zMAhLW
# icb8HI1Bng6wXfDufjrGocCRDZFz1ABWaM3Q1mm2cq2ncN0aLXm56aNQPBZDzQl8
# '''
# ssh_key_part2 = '''5D6TNdcIdkFcKYty2iXjqkauglhSDA5k4X3cgP7vM8WUYNWOzHv5vD0ljIvHpTx8
# 2oo6PUt1c9LBjt49hqw7kBBt8MOpGSoHgl7ZBH0= pen@ubuntu20'''

# commands = [f'conf t', f'ip ssh pubkey-chain', '\n', 'username admin', '\n', 'key-string', '\n', f'{ssh_key_part1}','\n', f'{ssh_key_part2}','\n','exit', 'exit', 'exit']


net_connect = Netmiko(**csr)
print("Connected successfully")
config = net_connect.send_config_set(commands,read_timeout=35)
print(config)
# print(net_connect.send_command('show ip int brief'))

''' Send config from file'''

# config = net_connect.send_config_from_file(config_file='config.txt')
# print(config)
# print(net_connect.send_command('show ip int brief'))