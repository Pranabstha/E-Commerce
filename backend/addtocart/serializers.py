from rest_framework import serializers
from .models import Cart


class AddToCartSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields = "__all__"



