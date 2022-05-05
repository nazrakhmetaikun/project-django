from django.db import models
from products.models import Products

class OrderManager(models.Manager):

    def filter_store_orders(self,store_id):
        orders = super().get_queryset().filter(items__product__store__id=store_id)
        # data = super().get_queryset().filter(id__in=data)
        return orders


    def filter_user_orders(self,user_id):
        return super().get_queryset().filter(user__id=user_id)

    
class OrderItemsManager(models.Manager):
    

    def create(self, **kwargs):
        kwargs['price'] = kwargs['product'].price
        return super().create(**kwargs)