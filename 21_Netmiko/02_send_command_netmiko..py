from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.23',
    'username': 'admin',
    'password': 'admin'
}

net_connect = Netmiko(**csr)
print("Connected successfully")

''' How to send commands to our router '''
# cmd_output = net_connect.send_command("show ip interface brief")
# print(cmd_output,"\n", net_connect.find_prompt()) #Prints the output and shows the prompt

''' Increase timeout when we expect more delay for command execution '''
cmd_output = net_connect.send_command("ping 1.2.3.4 repeat 5", read_timeout=15) 
print(cmd_output)

''' Expect string example with regular expression(RegEx). Command will fail if expected string is missing'''
cmd_output = net_connect.send_command("ping 1.2.3.4 repeat 5", read_timeout=15, expect_string=r"C.+#") #This will match hostname and enable mode
print(cmd_output)