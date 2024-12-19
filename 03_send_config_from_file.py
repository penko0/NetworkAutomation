import sys
import time
import paramiko
from paramiko import client, ssh_exception
import socket
import datetime


username = 'admin'
password = 'admin'

csr_cmd = ['show run']

with open('csr_config.txt', 'r') as config:
    new_commands = config.readlines()
    print(new_commands)

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
        for cmd in commands:
            device_access.send(f"{cmd}\n") #Here we send the commands to Cisco IOS interactive shell
            time.sleep(2) 
            output = device_access.recv(65535) #Here we define the output and its size in bytes
            print(output.decode(), end='') #Here we print the output , actually the IOS interactive shell

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

cisco_cmd_executor('192.168.1.172', new_commands)