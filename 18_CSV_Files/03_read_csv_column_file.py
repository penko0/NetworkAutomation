
from csv import reader
from pprint import pprint
import paramiko
import time

conf_dict = {}
with open('02_config_in_column.csv') as csv_data:
    csv_content = reader(csv_data)
    ips = next(csv_content)

    for conf in csv_content:
        for ip in ips:
            if not ip:
                continue
            if ip not in conf_dict.keys():
                conf_dict[ip] = list()
            n = ips.index(ip)

            if not conf[n]:
                continue
            conf_dict[ip].append(conf[n])
        # print(conf)

pprint(conf_dict)

session = paramiko.client.SSHClient()
session.load_system_host_keys()
session.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
for ip, conf_cmd in conf_dict.items():
    try:
        print(f"\n{'#' * 50}\nConnecting to the Device {ip}\n{'#' * 50} ")
        session.connect(hostname=ip,
                        username='admin',
                        password='admin',
                        look_for_keys=False,
                        allow_agent=False
                        )
        device_access = session.invoke_shell()
        print(f"\nExecuting Commands are\n{'~' * 22}\n{conf_dict[ip]}")
        for conf in conf_cmd:
            device_access.send(conf + '\n')
            time.sleep(1)
            output = device_access.recv(65000)
            print(output.decode('ascii'), end='')
            time.sleep(.5)
        session.close()
    except:
        print('Can not connect to the device')

print(f"\n{'#' * 50}\nCOMMAND EXECUTION COMPLETED\n{'#' * 50}\n")
