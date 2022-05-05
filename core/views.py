from rest_framework.views import APIView
from .serializers import RegistrationDataSerializer,AuthorizationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.hashers import check_password,make_password
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    methods=['post'],
    request_body=RegistrationDataSerializer
)
@api_view(['POST'])
def registrationview(request):
    serializer = RegistrationDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@swagger_auto_schema(
    methods=['post'],
    request_body=AuthorizationSerializer
)
@api_view(['POST'])
def authentication(request):
    serializer = AuthorizationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    filter_query = {}
    if serializer.data.get('email'):
        filter_query['email'] = serializer.data.get('email')
    if serializer.data.get('username'):
        filter_query['username'] = serializer.data.get('username')
    user = CustomUser.objects.filter(**filter_query)
    if not user.exists():
        return Response({"message":"Cant find with email or username"})
    user = user.first()
    if not check_password(serializer.data.get('password'),user.password):
        return Response({"message":"Password is not correct"})
    payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    get_token = api_settings.JWT_ENCODE_HANDLER
    payload = payload_handler(user)
    token = get_token(payload)
    return Response({'access_token':token})