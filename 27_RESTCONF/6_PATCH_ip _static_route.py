import json
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.23/restconf/data/Cisco-IOS-XE-native:native/ip/route"

host_dict = {
    "Cisco-IOS-XE-native:route": {
        "ip-route-interface-forwarding-list": [
            {
                "prefix": "1.1.3.10",
                "mask": "255.255.255.255",
                "fwd-list": [
                    {
                        "fwd": "GigabitEthernet1"
                    }
                ]
            }
        ]
    }
}
payload = json.dumps(host_dict)

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("PATCH", url, headers=headers, data=payload, verify=False)

print(response.status_code)
