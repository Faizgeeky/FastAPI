import requests 

# endpoint = "http://127.0.0.1:8000/api"
# get_response = requests.get(endpoint, params={'data':1234}, json={"query":"select from"})

# check basic home api
# print("result ", get_response.json())


# endpoint = "http://127.0.0.1:8000/api/add-product/"
# get_response = requests.post(endpoint, json={'titljje':"New Product 2"})
# print("result ", get_response.json())


endpoint = "http://127.0.0.1:8000/api/1"
get_response = requests.get(endpoint, json={'titljje':"New Product 2"}, params={'pk':1})
print("result we get here is ", get_response.json())