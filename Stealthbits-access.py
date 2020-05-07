import requests, urllib3, json, sys

URL = 'http://stealthbits/api/v1/token'


client_ID=''
client_secret=''

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
   
data = {	
    "grant_type":"client_credentials",
    "client_id": client_ID,
    "client_secret": client_secret 
        }

headers = {"Content-Type" : "application/json"}
print('data: {}'.format(data))
print('headers : {}'.format(headers))
print('url: {}'.format(URL))

try:
    response = requests.post(URL, data=json.dumps(data), verify=False, timeout=3, auth=(client_ID, client_secret), headers=headers)
except requests.exceptions.ConnectionError as err:  
    print('Error: {}'.format(err))
    sys.exit()
print('Response: {}'.format(response))
