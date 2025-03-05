from rest_framework import serializers
from .models import BaseUser

class BaseUserSerializer(serializers.ModelSerializer):
    """Base serializer to avoid code duplication."""
    
    class Meta:
        model = BaseUser
        fields = ["id", "email", "first_name", "last_name"]
        extra_kwargs = {
            "email": {"read_only": True},
        }

class UserListSerializer(serializers.ModelSerializer):
    """Serializer for listing users with minimal fields."""
    class Meta:
        model = BaseUser
        fields = ["id", "email"]

class UserListFilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    is_admin = serializers.BooleanField(required=False, allow_null=True, default=None)
    email = serializers.EmailField(required=False)

class UserDetailSerializer(BaseUserSerializer):
    """Serializer for retrieving user details."""
    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ["is_admin"]

class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration with password confirmation."""
    password1 = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = BaseUser
        fields = ['email', 'password1', 'password2']

    def validate(self, data):
        """Ensure passwords match before saving."""
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password2": "Passwords do not match."})
        return data

    def create(self, validated_data):
        """Remove password2 and hash password before creating user."""
        validated_data.pop('password2')
        return BaseUser.objects.create_user(email=validated_data['email'], password=validated_data['password1'])


class UserUpdateSerializer(BaseUserSerializer):
    """Serializer for updating user details."""
    
    class Meta(BaseUserSerializer.Meta):
        fields = ['first_name', 'last_name']

class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ["id"]
