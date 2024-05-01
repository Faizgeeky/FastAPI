import requests 

# endpoint = "http://127.0.0.1:8000/api"
# get_response = requests.get(endpoint, params={'data':1234}, json={"query":"select from"})

# check basic home api
# print("result ", get_response.json())


# endpoint = "http://127.0.0.1:8000/api/add-product/"
# get_response = requests.post(endpoint, json={'titljje':"New Product 2"})
# print("result ", get_response.json())


# endpoint = "http://127.0.0.1:8000/api/1"
# get_response = requests.get(endpoint, json={'titljje':"New Product 2"}, params={'pk':1})
# print("result we get here is ", get_response.json())

# endpoint = "http://127.0.0.1:8000/api/"
# get_response = requests.post(endpoint, json={'title':"New Product 5",'price':199.22}, params={'pk':1})
# print("result we get here is ", get_response.json())

# List Product
# endpoint = "http://127.0.0.1:8000/api/list-products/"
# get_response = requests.get(endpoint, json={'sss':"New Product 5",'price':199.22}, params={'pk':1})
# print("result we get here is ", get_response.json())

# # Update Product
# endpoint = "http://127.0.0.1:8000/api/update-product/1"
# get_response = requests.put(endpoint, json={'title':" fresh?",'price':19.5}, params={'pk':1})
# print("result we get here is ", get_response.json())

# Delete Product
endpoint = "http://127.0.0.1:8000/api/delete-product/4"
get_response = requests.delete(endpoint, json={'title':" fresh?",'price':19.5}, params={'pk':1})
print(get_response.status_code,get_response.status_code==204 )