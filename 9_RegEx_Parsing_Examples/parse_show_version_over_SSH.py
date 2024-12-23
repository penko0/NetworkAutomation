import sys
import time
import paramiko
from paramiko import client, ssh_exception
import socket
import datetime
import re

#Defining RegExp. Use for test on CSR router
version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)')
model_pattern = re.compile(r'cisco (\S+).+bytes of memory\.')
serial_number_pattern = re.compile(r'Processor board ID (\S+)')
uptime_pattern = re.compile(r'(.+) uptime is (.*)')



username = 'admin'
password = 'admin'

new_cmd = ['show version']

def cisco_cmd_executor(hostname, commands):
    try:
        print(f"Connecting to the device {hostname}..")
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                           allow_agent=False)

        print(f"Connected to the device {hostname}")
        device_access = ssh_client.invoke_shell() #Here we invoke the real shell and can see it in the configured output
        device_access.send("terminal len 0\n")
        with open('current_config_file', 'w') as cmd_data:
            for cmd in commands:
                device_access.send(f"{cmd}\n") #Here we send the commands to Cisco IOS interactive shell
                time.sleep(2) 
                output = device_access.recv(65535).decode() #Here we define the output and its size in bytes
                cmd_data.write(output)
                print(output) #Here we print the output , actually the IOS interactive shell

                ssh_client.close()
        
                version_match = version_pattern.search(output)
                print(version_match)
                print('IOS Version:'.ljust(18) + str(version_match))
                model_match = model_pattern.search(output)
                print('Router model is:'.ljust(18) + str(model_match.group(1)))
                serial_number_match = serial_number_pattern.search(output)
                print('Serial number is:'.ljust(18) + str(serial_number_match.group(1)))
                uptime_match = uptime_pattern.search(output)
                print('Hostname is:'.ljust(18) + str(uptime_match.group(1)))
                print('Device uptime is:'.ljust(18) + str(uptime_match.group(2)))
    except ssh_exception.NoValidConnectionsError:
        print("SSH Port not reachable")
    except socket.gaierror:
        print("Check the hostname")
    except ssh_exception.AuthenticationException:
        print("Authentication failed, check credentials")

    except:
        print("Exception Occurred")
        print(sys.exc_info())
        # traceback.print_exception(*sys.exc_info())

cisco_cmd_executor('192.168.1.23', new_cmd)