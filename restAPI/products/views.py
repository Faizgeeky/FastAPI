from django.shortcuts import render
# from django.http import JsonResponse
from products.models import Product
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from rest_framework import generics , mixins



# @api_view(['GET','POST'])
# def home(request):
#     '''
#     DRF API VIEW
#     '''

#     # data = 
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     # Method 1 manual
#     # if model_data:
#     #     data['id'] = model_data.id
#     #     data['title'] = model_data.title
#     #     data['content'] = model_data.content
#     #     data['price'] = model_data.price
#     # print("Model data is ", model_data.title)

#     # Method 3 model_to_dict
#     # if model_data:
#     #     data = model_to_dict(model_data, fields=['id','title', 'price', 'sale_price'])
    
#     # Method 3 Serializers
#     instance = model_data

#     if instance:
#         data =  ProductSerializer(instance).data


#     return Response(data)


# #  Validation using Serializer
@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data = request.data)
    # Use raise expceptions to handle invalid or error in robust way
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print("Instance is here", instance)
        return Response(serializer.data)



# Generic RetriveAPI View 
#this will return data without handling or sending back the response 
class ProductDetailAPIView(generics.RetrieveAPIView):
    print("view test 1")
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.sa

# Generic CreateAPI View
class ProductCreateAPIView(generics.CreateAPIView):
    print("view test 2")
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_create_view = ProductCreateAPIView.as_view()

#Genericc ListAPIView and ListcreateAPIView
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# list view 
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Update API View 
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        

#  Mixins in DRF 
# Provide multiple mixins if required like following example
class ProductMixinView(mixins.CreateModelMixin ,mixins.ListModelMixin , mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self , request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     print("Args",args, kwargs)
    #     pk = kwargs.get("pk")
    #     print("pk is", pk)
    #     if pk is not None:
    #         return self.retrieve(request, *args, **kwargs)
        
    #     return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title =  serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        
        