from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework import generics
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         user = User.objects.get(id=token.user_id)
#         return Response({'token': token.key, 'user':  UserSerializer(user).data})


# class RegisterView(APIView):

#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         user = User(username=username)
#         user.set_password(password)
#         user.save()
#         refresh = RefreshToken.for_user(user)

#         return Response(
#             {
#                 "status":"Success",
#                 'user_id':user.id,
#                 'refresh':str(refresh),
#                 'access':str(refresh.access_token)
#             })