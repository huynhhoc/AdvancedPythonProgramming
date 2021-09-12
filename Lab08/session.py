import requests
session = requests.Session()

a_header = {"sample_header": "sample_value"}
session.headers.update(a_header)

response = session.get("https://kite.com", headers=session.headers)

print(response.request.headers["sample_header"])

print(response)

import requests

url = 'https://w3schools.com/python/demopage.php'

#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.get(url, auth = ('user', 'pass'))

print(x.status_code)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r)
