from django.db import models
import uuid
from .managers import OrderManager,OrderItemsManager

class Orders(models.Model):
    uuid = models.UUIDField("UUID",primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("users.CustomUser",related_name="orders",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)

    objects = OrderManager()

    def get_total_cost(self):
        total = sum( item.get_cost() for item in self.items.all())
        return total

class OrderItems(models.Model):
    order = models.ForeignKey("orders.Orders",on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey("products.Products",related_name="orders",on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()

    objects = OrderItemsManager()

    def get_cost(self):
        return self.price * self.quantity