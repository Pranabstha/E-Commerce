from django.urls import include, path
from .views import ItemDetails
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('items/', ItemDetails.as_view(), name='items'),
]