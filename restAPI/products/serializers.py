from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Product


class ProductSerializer(ModelSerializer):
    # enrich with other name to any filed 
    discounted_price = SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['title','content','price','sale_price','discounted_price']

    def get_discounted_price(self, obj):
        try:
            return obj.get_discount()
        except:
            return None