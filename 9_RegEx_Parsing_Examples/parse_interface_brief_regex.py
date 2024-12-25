import sys
import time
import traceback
from paramiko import client, ssh_exception
from getpass import getpass
import socket
import datetime
import re
from pprint import pprint

int_pattern = re.compile(r'(\S+)\s+(([\d\.]+)|unassigned)\s+\S+\s+\S+\s+(up|administratively down)\s+(\S+)')  #Use regex101.com to create regular expressions

new_cmd = ['show ip interface brief']

def cisco_cmd_executor(hostname, commands, username, password):
    try:
        print(f"Connecting to the device {hostname}..")
        now = datetime.datetime.now().replace(microsecond=0)
        current_conf_file = f"{now}_{hostname}.txt"
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                           allow_agent=False)

        print(f"Connected to the device {hostname}")
        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n")
        with open(current_conf_file, 'w') as cmd_data:
            for cmd in commands:
                device_access.send(f"{cmd}\n")
                time.sleep(3)
                output = device_access.recv(65535).decode()
                #cmd_data.write(output)
                print(output)
        ssh_client.close()
        print(int_pattern.search(output)) #This will print the first match 
        int_iteration = int_pattern.finditer(output) # When we have more that one interfaces , we must use finditer() along with "for" cycle to print the end result that is saved to list
        int_list = list()
        for intf in int_iteration:
            int_dict = dict()
            print(intf.group(1), intf.group(2), intf.group(4))
            int_dict['name'] = intf.group(1)
            int_dict['ip'] = intf.group(2)
            int_dict['status'] = intf.group(4)
            int_list.append(int_dict)
        pprint(int_list)
        
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
cisco_cmd_executor('192.168.1.23', new_cmd, 'admin', 'admin')