from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser,Stores
from .serializers import StoreSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from drf_yasg.utils import swagger_auto_schema
class UserView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


    def get_object(self):
        obj = get_object_or_404(CustomUser,id=self.request.user.id)
        return obj

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(methods=['POST'])
def password_update(self,request):
    user = request.user
    if request.data.get('password') is None:
        return Response({"message":"Password not sended"})
    user.set_password(request.data.get['password'])
    return Response()

class StoresView(generics.CreateAPIView,generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer
    queryset = Stores.objects.all()


    def get_object(self):
        obj = get_object_or_404(Stores,user=self.request.user)
        return obj
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)