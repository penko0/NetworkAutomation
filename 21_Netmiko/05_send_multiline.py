#Here we use ConnectHandler
from netmiko import ConnectHandler

#Router`s login details in dictionary format 
csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}

net_connect = ConnectHandler(**csr)
print("Connected Successfully")

''' Send multiple show commands at once'''
# cmd_output = net_connect.send_multiline(['show ver','show ip int br'])
# print(cmd_output)

copy_cmd = 'copy bootflash:csr1000v-mono-universalk9.17.03.04a.SPA.pkg bootflash:new.pkg'
copy_cmd_expect = r"Destination filename"
#commands and their "expected_string" that we expect on router`s console
cmd_list = [[copy_cmd, copy_cmd_expect], ['\n', r'Copy in progress...\S+\s']] #Here we use RegEx to match the output of copy process. Use www.regex101.com for RegEx configuration

cmd_output = net_connect.send_multiline(cmd_list, read_timeout = 50)
print(cmd_output)

#The script works but ends with errors because of the expected strig problems