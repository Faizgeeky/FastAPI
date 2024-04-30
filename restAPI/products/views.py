from django.shortcuts import render
# from django.http import JsonResponse
from products.models import Product
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(['GET','POST'])
def home(request):
    '''
    DRF API VIEW
    '''
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    # Method 1 manual
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    # print("Model data is ", model_data.title)

    # Method 3 model_to_dict
    # if model_data:
    #     data = model_to_dict(model_data, fields=['id','title', 'price', 'sale_price'])
    
    # Method 3 Serializers
    instance = model_data

    if instance:
        data =  ProductSerializer(instance).data


    return Response(data)


def addProduct(request):
    data = request.GET
    message = ''
    try:
        if data['price'] and data['content'] and data['title']:
            model_data = Product.objects.create(title=data['title'],content=data['content'],price=data[price])
            model_data.save()
            message = 'Data added'
        else:
            message = "No data is  added"
    except:
        pass
    print("data is ", data)
    return Response({'message':message})