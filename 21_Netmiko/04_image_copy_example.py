from netmiko import Netmiko

#Router`s login details in dictionary format 
csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}

copy_cmd = 'copy bootflash:csr1000v-mono-universalk9.17.03.04a.SPA.pkg bootflash:new.pkg'
net_connect = Netmiko(**csr)
print ("Connected Successfully")

#Start the copy process and expects a comand promt with question for destination file name
run_df = net_connect.send_command(copy_cmd, expect_string="Destination filename")
print(run_df)

''' Use it only if you already have a file with the same name '''
# run_overwrite = net_connect.send_command("\n", expect_string="Do you want to over write")
# print(run_overwrite)
''' Equals to pressing enter on the terminal.'''
run_c = net_connect.send_command("\n", read_timeout=50)
print(run_c)