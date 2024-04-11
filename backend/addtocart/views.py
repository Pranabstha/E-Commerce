from .serializers import AddToCartSerializers
from rest_framework.views import APIView
from rest_framework import status
from .models import Cart
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class AddToCart(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        if user:
            serializer = AddToCartSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({
                "error" : False,
                "status" : "item added to cart successfully"
                # 'data': 
            }, status= status.HTTP_200_OK)
        else:
            return Response({
                "error" : False,
                "data" : 'Unable to add to cart',
                "status" : status.HTTP_401_UNAUTHORIZED
            },status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        user = request.user
        if user:
            obj = Cart.objects.all()
        else:
            obj = Cart.objects.filter(user=user)
        if obj:
            serailizer = AddToCartSerializers(obj, many=True)
            return Response({
                "error" : False,
                "data": serailizer.data,
                "status" : "User cart item"
                }, status= status.HTTP_200_OK)
        return Response({
            'error': True,
            'data': 'Unable to add to cart',
            'status': status.HTTP_400_BAD_REQUEST   
        },status=status.HTTP_400_BAD_REQUEST) 
    

    def delete(self, request):
        user = request.user
        # print(user)
        try:
            id = request.data['id']
        except:
            return Response({
            'error': True,
            'data': 'No items in cart',
            'status': status.HTTP_400_BAD_REQUEST   
            },status=status.HTTP_400_BAD_REQUEST) 
        try:
            obj = AddToCart.objects.get(id=id)
        except:
            return Response({
            'error': True,  
            'data': 'No items in cart',
            'status': status.HTTP_400_BAD_REQUEST   
            },status=status.HTTP_400_BAD_REQUEST) 
        obj.delete()
        return Response({
            "error" : False,
            "data": "data deleted successfully",
            "status" : "User cart item"
            }, status= status.HTTP_200_OK)


    def patch(self, request):
        user = request.user
        if user:
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
                obj = AddToCart.objects.get(id=id)
            except: 
                return Response({
                'error': True,
                'data': 'The item is not presnet',
                'status': status.HTTP_400_BAD_REQUEST   
            },status=status.HTTP_400_BAD_REQUEST)            
            serailize = AddToCartSerializers(obj, data=request.data, partial = True)
            if serailize.is_valid():
                serailize.save()        
                return Response({
                    'error': False,
                    'data':'item updated successfully', 
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
                    'data': 'You dont have the access to perform this operation',
                    'status': status.HTTP_400_BAD_REQUEST,  
                }, status=status.HTTP_400_BAD_REQUEST)
 
        
        

