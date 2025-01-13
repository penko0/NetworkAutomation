import requests
import json

url = "https://192.168.1.174/ins"

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "bash",
    "chunk": "0",
    "sid": "sid",
    "input": "cat /etc/os-release",
    "output_format": "json"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)