
from rest_framework.response import Response# type: ignore
from django.contrib.auth import authenticate,login, logout# type: ignore
from .models import User
from .serializers import UserSerializer
from rest_framework import generics# type: ignore
from rest_framework.permissions import IsAdminUser# type: ignore
from rest_framework.views import APIView# type: ignore
from rest_framework import status# type: ignore
from rest_framework.permissions import AllowAny, IsAuthenticated# type: ignore
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore


class UserDetails(APIView):
    def post(self, request):
        print(request.data,"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        serializer = UserSerializer(data=request.data)
        print("0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0")
        if serializer.is_valid():
            serializer.save()          
            return Response(
                {
                    'error': False,
                    'data': serializer.data,
                    'message': 'User has successfully been created.',
                    'status': status.HTTP_201_CREATED
                },
                status=status.HTTP_201_CREATED)
        return Response(
            {
                'error': True,
                'message': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self,request):
        print(request.data)
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

        


