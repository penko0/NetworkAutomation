import json
from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.23/restconf/data/Cisco-IOS-XE-native:native"

headers = {
    'Accept': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46YWRtaW4='
}
''' Here we can specify user and password in "response" var instead of using "headers" var '''
# response = requests.request("GET", url, headers=headers, verify=False, auth = ('admin', 'admin'))
response = requests.request("GET", url, headers=headers, verify=False)

dict_data = response.json()
print(dict_data)

with open('conf.json', 'w') as conf:
    json.dump(dict_data, conf, indent=4)
