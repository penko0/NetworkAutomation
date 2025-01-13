import json
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = "https://192.168.1.25/restconf/data/Cisco-IOS-XE-native:native/ip/domain"

host_dict = {"name": "test2.com"}
payload = json.dumps(host_dict)

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.status_code)
