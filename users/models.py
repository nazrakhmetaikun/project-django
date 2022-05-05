from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import AbstractModel
from django.core.validators import RegexValidator

PhoneNumberValidator = RegexValidator(regex = r"^\+?1?\d{8,15}$")


class CustomUser(AbstractUser):
    favourites = models.ManyToManyField("products.Products",related_name="user")
    phone_number = models.CharField(validators=[PhoneNumberValidator],max_length=18)



class Stores(AbstractModel):
    user = models.OneToOneField("users.CustomUser",related_name="store",on_delete=models.CASCADE)
    address = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    description = models.TextField()
    contact_phone_number = models.CharField(max_length=18,validators=[PhoneNumberValidator])
    logo = models.ImageField(upload_to="logo/",null=True)