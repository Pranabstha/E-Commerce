from django.urls import include, path
from .views import UserDetails,UserLogin
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', UserDetails.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login')
]