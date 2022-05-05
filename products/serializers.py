from rest_framework import serializers
from .models import Products, Subcategory

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ("id","name")


class ProductDetailSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.CharField(source="subcategory.name",read_only=True)
    store = serializers.CharField(source="store.name",read_only=True)

    class Meta:
        model = Products
        fields = ('id','name','description','price','subcategory_name','subcategory','store')