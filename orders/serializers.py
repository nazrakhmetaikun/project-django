from rest_framework import serializers
from .models import Orders,OrderItems
from users.models import CustomUser
from products.models import Products

class OrderList(serializers.ModelSerializer):

    total = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        fields = ('uuid','created_at','paid','total')

    def get_total(self,obj):
        return obj.get_total_cost()


class OrderItemsSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source="product.name",read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = OrderItems
        fields = ('product','product_name','price','quantity','total')

        extra_kwargs = {
            'price': {'read_only':True,}
        }
    
    def get_total(self,obj):
        return obj.get_cost()
    

    def create(self,validated_data):
        validated_data['price']= Products.objects.get(id=validated_data['product']).price
        instance = OrderItems.objects.create(**validated_data)
        return instance


class OrderDetial(serializers.ModelSerializer):

    items = OrderItemsSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        fields = ('items','created_at','paid','total')

    def get_total(self,obj):
        return obj.get_total_cost()
    

    def create(self,validated_data):
        items = validated_data.pop('items')
        instance = Orders.objects.create(**validated_data)
        for item in items:
            OrderItems.objects.create(**item,order=instance)
        return instance