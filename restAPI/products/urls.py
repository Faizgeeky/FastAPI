from django.urls import path
from . import views
urlpatterns = [
    # path("", views.home, name="home"), 
    # path("add-product/", views.addProduct, name="add-product"), 
    # Concrete API Views
    path('<int:pk>/',views.ProductDetailAPIView.as_view(), name="Genric retrive api view"),
    path('',views.product_create_view, name="Genric creare api view"),
    path('create-list-products/',views.ProductListCreateAPIView.as_view(), name="Genric create LIST api view"),
    path('list-products/',views.ProductListAPIView.as_view(), name="Genric only LIST api view"),
    path('update-product/<int:pk>',views.ProductUpdateAPIView.as_view(), name="Genric Update api view"),
    path('delete-product/<int:pk>',views.ProductDestroyAPIView.as_view(), name="Genric Update api view"),

    # Mixins 
    path('products/<int:pk>/',views.ProductMixinView.as_view(), name="Mixin view LIST view"),

]
