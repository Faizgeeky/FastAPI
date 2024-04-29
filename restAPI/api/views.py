from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def home(request):
    print("data is ", request.body)
    print("data is ", request)

    body = request.body
    data = {}
    try:
        data =  json.loads(body)
    except:
        pass
    print("Data is here", data , data.keys())
    print("Params", request.GET)
    return JsonResponse({"message":"Hello world"})