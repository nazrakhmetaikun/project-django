from core.serializers import NameAndIdSerializer
from .models import Category,Subcategory,Products
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action,permission_classes
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from users.models import  Stores
from drf_yasg.utils import swagger_auto_schema
from .serializers import ProductDetailSerializer, ProductListSerializer
from .permissions import HasStore

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        data = Category.objects.all()
        serializer = NameAndIdSerializer(data,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        data = Category.objects.get_subcategories(id=pk)
        data = Subcategory.objects.filter(id__in=data)
        serializer = NameAndIdSerializer(data,many=True)
        return Response(serializer.data)

class SubcategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        data = Subcategory.objects.all()
        serializer = NameAndIdSerializer(data,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        data = Products.objects.filter_by_subcategory(id_list=[pk])
        serializer = ProductListSerializer(data,many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):


    def list(self,request):
        data = Products.objects.all()
        serializer = ProductListSerializer(data,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk):
        data = get_object_or_404(Products,pk=pk)
        serializer = ProductDetailSerializer(data)
        return Response(serializer.data)
    

    @action(methods=['POST'],detail=False,renderer_classes=[JSONRenderer])
    @permission_classes([IsAuthenticated,HasStore])
    @swagger_auto_schema(request_body=ProductDetailSerializer)
    def add_own_product(self,request):
        store = get_object_or_404(Stores,user=request.user)
        serializer = ProductDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(store=store)
        return Response(serializer.data)