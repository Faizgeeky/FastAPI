import requests 

endpoint = "http://127.0.0.1:8000/api"
get_response = requests.get(endpoint, params={'data':1234}, json={"query":"select from"})

# check basic home api
print("result ", get_response.json()['message'])