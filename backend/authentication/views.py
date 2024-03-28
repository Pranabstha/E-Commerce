
from rest_framework.response import Response
from django.contrib.auth import authenticate,login, logout
from .models import User
from .serializers import UserSerializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserDetails(APIView):
    serializer_class = UserSerializers

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.set_password(obj.password)
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            'error': True,
            'data': 'Unable to create user',
            'status': status.HTTP_400_BAD_REQUEST   
        },status=status.HTTP_400_BAD_REQUEST) 
    

class UserLogin(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate( email = email, password = password)
        if user:
            login(request,user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'error': False,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'data': 'login successfull',
                'status': status.HTTP_200_OK   
            },status=status.HTTP_200_OK)
        return Response({
            'error': True,
            'data': 'log In failed',
            'status': status.HTTP_400_BAD_REQUEST   
            },status=status.HTTP_400_BAD_REQUEST)       

        


