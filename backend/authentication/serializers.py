from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = "__all__"




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        """
        Check if the email address already exists in the database.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address already in use")
        return value

    def create(self, validated_data):
        """
        Create a new user instance.
        """
        user = User.objects.create_user(**validated_data)
        return user
