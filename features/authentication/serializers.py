from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
