import sys
import time
#import paramiko
from paramiko import client, ssh_exception
import socket
import datetime


username = 'admin'
password = 'admin'
csr_cmd = ['show run', 'show ip int brief']
with open('show_commands.txt') as show_commands:
    sh_commands = show_commands.readlines()


def cisco_cmd_executor(hostname, commands):
    try:
        print(f"Connecting to device {hostname}..")
        now = datetime.datetime.now().replace(microsecond=0)
        current_conf_file = f"{now}_{hostname}.txt"
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                           allow_agent=False)

        print(f"Connected to device {hostname}")
        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n")
        for cmd in enumerate(commands, start=1):
            file_name = f"{str(now).replace(' ', ':')}_{str(cmd[0]).zfill(2)}_{cmd[1].replace(' ', '_').strip()}.txt"
            with open(file_name, 'w') as cmd_data:
                device_access.send(f"{cmd[1]}\n")
                time.sleep(3)  #Due to latency of the router we have to increase the sleep time in order to receive the whole running config
                output = device_access.recv(65535)
                cmd_data.write(output.decode()) #Decodes byte data to UTF format
                print(output.decode(), end='')

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

cisco_cmd_executor('192.168.1.23', sh_commands)