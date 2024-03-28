from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ItemSerializers
from rest_framework.views import APIView
from rest_framework import status
from .models import Items
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class ItemDetails(APIView):
    permission_classes = (IsAuthenticated,)


    def post(self, request):
        user = request.user
        if user.is_superuser and user.is_staff:
            serializer = ItemSerializers(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                serialized_data = ItemSerializers(obj).data
                return Response({"error": False,
                                "data": serialized_data, 
                                "status":"Items added successfull"
                                },status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response({
                    'error': True,
                    'data': 'Unable to register items',
                    'status': status.HTTP_400_BAD_REQUEST,
                    'error': serializer.error_messages   
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                    'error': True,
                    'data': 'only admins and customer are able to perform this operation',
                    'status': status.HTTP_400_BAD_REQUEST,  
                }, status=status.HTTP_400_BAD_REQUEST)    
        

    def get(self, request):
        user = request.user
        if user.is_customer or user.is_superuser:
            obj = Items.objects.all()
        else:
            obj = Items.objects.filter(user=user)
        if obj:
            serailize = ItemSerializers(obj, many=True)
            return Response({
                'error': False,
                'data':serailize.data,
                'status':status.HTTP_200_OK
            },status=status.HTTP_200_OK)
        return Response({
            'error': True,
            'data': 'Item unavaliable',
            'status': status.HTTP_400_BAD_REQUEST   
        },status=status.HTTP_400_BAD_REQUEST)   


    def patch(self, request):
        user = request.user
        if user.is_superuser and user.is_staff:
            try:
                id = request.data['id']
            except:
                return Response({
                    'error': True,
                    'data': 'id required',
                    'status': status.HTTP_400_BAD_REQUEST   
                },
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                obj = Items.objects.get(id=id)
            except: 
                return Response({
                'error': True,
                'data': 'The item is not presnet',
                'status': status.HTTP_400_BAD_REQUEST   
            },status=status.HTTP_400_BAD_REQUEST)            
            serailize = ItemSerializers(obj, data=request.data, partial = True)
            if serailize.is_valid():
                serailize.save()        
                return Response({
                    'error': False,
                    'data':'item uopdated successfully', 
                    'status':status.HTTP_200_OK
                },status=status.HTTP_200_OK)
            else: 
                return Response({
                'error': True,
                'data': 'Unable to update',
                'status': status.HTTP_400_BAD_REQUEST   
            },status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response({
                    'error': True,
                    'data': 'only admins and customer are able to perform this operation',
                    'status': status.HTTP_400_BAD_REQUEST,  
                }, status=status.HTTP_400_BAD_REQUEST)           


    def delete(self, request):
        user = request.user
        if user.is_superuser and user.is_staff:
            try:
                id = request.data['id']

            except:
                return Response({
                    'error': True,
                    'data': 'id required',
                    'status': status.HTTP_400_BAD_REQUEST   
                },
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                obj = Items.objects.get(id=id)
            except: 
                return Response({
                'error': True,
                'data': 'blog not found.',
                'status': status.HTTP_400_BAD_REQUEST   
            },status=status.HTTP_400_BAD_REQUEST)            

            obj.delete()      
            return Response({
                'error': False,
                'data':'Deleted Successfully', 
                'status':status.HTTP_200_OK
            },status=status.HTTP_200_OK)
        else:
            return Response({
                    'error': True,
                    'data': 'only admins and customer are able to perform this operation',
                    'status': status.HTTP_400_BAD_REQUEST, 
                }, status=status.HTTP_400_BAD_REQUEST)       

  
