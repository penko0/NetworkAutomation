import json
from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.23:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
# print(dir(response))
# print(type(response))
# print(type(response.text))
# print(type(response.json()))

# t = response.text
# dict_data = json.loads(t)

dict_data = response.json()
int_list = dict_data['Cisco-IOS-XE-native:GigabitEthernet']
pprint(int_list)
for intf in int_list:
    try:
        print("GigabitEthernet"+intf['name'], intf['ip']['address']['primary']['address'])
    except KeyError:
        continue