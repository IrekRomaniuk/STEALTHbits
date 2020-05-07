import requests, urllib3, json, sys

URL = 'http://stealthbits/api/v1/data'
PATH = '/SA_4-SQL_ServerLogons_Logons/rows'
PATH = '/SA_ADInventory_ComputersView/rows'



access_token="Bearer ABC"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {"Content-Type" : "application/json", "Authorization": access_token}

print('headers : {}'.format(headers))
print('url: {}'.format(URL + PATH))

try:
    response = requests.get(URL + PATH, verify=False, timeout=3, headers=headers)
except requests.exceptions.ConnectionError as err:  
    print('Error: {}'.format(err))
    sys.exit()
print('Response: {}'.format(response))