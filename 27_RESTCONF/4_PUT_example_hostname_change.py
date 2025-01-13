import json
from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.25:443/restconf/data/Cisco-IOS-XE-native:native/hostname"

# ##### From dictionary
# host_dict = {"hostname": "csr2223"}
# payload = json.dumps(host_dict)

# ###### Send from multiline string
# payload = """{"hostname": 
# "csr23"}"""

# ###### Send config from file
# with open('host.json') as host:
#     payload = host.read()

###### Send  hostname config via user input
host_input = input("Enter hostname: ")
host_dict = {"hostname": host_input}
payload = json.dumps(host_dict)

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

print(response.status_code)
