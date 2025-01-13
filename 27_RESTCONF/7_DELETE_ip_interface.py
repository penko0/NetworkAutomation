import json
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.25/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=2"


headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("DELETE", url, headers=headers, verify=False)

print(response.text)
print(response.status_code)
print(response.reason)
