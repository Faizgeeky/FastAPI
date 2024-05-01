from django.urls import path
from . import views
urlpatterns = [
    # path("", views.home, name="home"), 
    # path("add-product/", views.addProduct, name="add-product"), 
    path('<int:pk>/',views.ProductDetailAPIView.as_view(), name="Genric api view"),

]
