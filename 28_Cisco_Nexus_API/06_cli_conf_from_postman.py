import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.174/ins"

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "sid",
    "input": "interface e1/2 ; description from-jsonrpc ; aaa ; no switchport ; ip add 1.1.1.1 255.255.255.0",
    "output_format": "json",
    "rollback": "continue-on-error" ### rollback-on-error does not work properly and I changed it to "continue-on-error"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)