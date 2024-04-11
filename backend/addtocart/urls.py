from django.urls import include, path
from .views import AddToCart
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('addtocart/', AddToCart.as_view(), name='addtocart'),
]