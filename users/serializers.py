from rest_framework import serializers
from .models import CustomUser, Stores
import re

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser
        fields = ("id","first_name","last_name","email")

        extra_kwargs = {
            "id": { "read_only" : True },
        }



class StoreSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(required=False)

    class Meta:
        model = Stores
        fields = ("id","name","description","lat","lng","contact_phone_number","logo")

        extra_kwargs = {
            "id": {"read_only": True}
        }
    
    def validate(self,data):
        errors = {}
        if data.get("contact_phone_number") is None:
            errors['contact_phone_number'] = "Not Send"
        else:
            if re.search(r"^\+?1?\d{8,15}$",data.get("contact_phone_number")) is None:
                errors["contact_phone_number"] = "Not correct format"
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
    def create(self,validated_data):
        instance = Stores.objects.create(**validated_data)
        return instance