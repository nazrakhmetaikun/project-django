from django.db import models

class ProductManager(models.Manager):

    def filter_by_subcategory(self,id_list):
        return self.filter(subcategory__id__in=id_list).order_by("-price")
    

    def filter_by_category(self,id_list):
        return self.filter(subcategory__category__id__in=id_list).order_by("-price")


class CategoryManager(models.Manager):

    def get_subcategories(self,id):
        return self.filter(id=id).values_list("subcategories",flat=True)

