from unicodedata import category
from django.db import models
from core.models import AbstractModel
from .managers import ProductManager,CategoryManager


class Category(AbstractModel):
    pass

    objects = CategoryManager()

class Subcategory(AbstractModel):
    category = models.ForeignKey("products.Category",related_name="subcategories",on_delete=models.CASCADE)

class Products(AbstractModel):
    subcategory = models.ForeignKey("products.Subcategory",on_delete=models.SET_NULL,related_name="products",null=True)
    price = models.IntegerField()
    description = models.TextField(null=True)
    store = models.ForeignKey("users.Stores",related_name="products",on_delete=models.CASCADE)


    objects = ProductManager()