from django.shortcuts import get_object_or_404
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from .models import Orders
from rest_framework.decorators import action,permission_classes
from .serializers import OrderDetial,OrderList
from drf_yasg.utils import swagger_auto_schema
from products.permissions import HasStore


class OrdersViewSet(viewsets.ViewSet):

    queryset = Orders.objects.all()

    @permission_classes([permissions.IsAuthenticated])
    def retrieve(self,request,id,*args, **kwargs):
        data = get_object_or_404(Orders,id=id)
        serializer = OrderDetial(data)
        return Response(serializer.data)

    @permission_classes([permissions.IsAuthenticated])
    def list(self,request,*args,**kwargs):
        data = Orders.objects.filter(user=request.user)
        serializer = OrderList(data, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=OrderDetial,responses={200:OrderDetial}
    )
    def create(self,request,*args,**kwargs):
        serializer = OrderDetial(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)

    @permission_classes([permissions.IsAuthenticated])
    def destroy(self,request,id,*args,**kwargs):
        instance = get_object_or_404(Orders,id=id)
        instance.canceled=True
        return Response()
    

    @action(detail=False,methods=['GET'])
    @permission_classes([permissions.IsAuthenticated,HasStore])
    @swagger_auto_schema(responses={200:OrderDetial(many=True)})
    def get_store_orders(self,request):
        store = request.user.store
        data = Orders.objects.filter_store_orders(store_id=store.id)
        serializer = OrderDetial(data,many=True)
        return Response(serializer.data)
    
    @action(detail=False,methods=['GET'])
    @swagger_auto_schema(responses={200:OrderDetial(many=True)})
    @permission_classes([permissions.IsAuthenticated])
    def get_user_order(self,request):
        data = Orders.objects.filter_user_orders(user_id=request.user.id)
        serializer = OrderDetial(data,many=True)
        return Response(serializer.data)
