#Here we use ConnectHandler for our SCP transfer
from netmiko import ConnectHandler, file_transfer, progress_bar

#Router`s login details in dictionary format 
csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}
net_connect = ConnectHandler(**csr)
print("Connected Successfully")

''' File transfer to our router'''
# transfer = file_transfer(net_connect,
#                          source_file='config.txt',
#                          dest_file='config_txt',
#                          file_system='bootflash:',
#                          direction='put',
#                          overwrite_file=True,
#                          progress4=progress_bar)

''' File transfer from our router to PC'''
transfer = file_transfer(net_connect,
                         source_file='running-config',
                         dest_file=f'running-config-{csr["host"]}', #Here we add the hostname to our detination file name
                         file_system='system:',
                         direction='get',
                         overwrite_file=True,
                         progress4=progress_bar)

print(transfer)
net_connect.disconnect()

