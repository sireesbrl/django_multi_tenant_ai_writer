from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BaseUser
from .serializers import *

from features.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)

from features.users.permissions import (
    IsAdminOrOwner,
    IsBaseUser,
    IsAdminUser,
)

from features.users.selectors import user_list, user_get

class UserListApi(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserListSerializer
    queryset = BaseUser.objects.all()

    class Pagination(LimitOffsetPagination):
        default_limit = 1

    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = UserListFilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=users,
            request=request,
            view=self,
        )

class UserDetailApi(generics.RetrieveAPIView):
    permission_classes = [IsAdminOrOwner]
    queryset = BaseUser.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer

class UserCreateApi(generics.CreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminOrOwner]
    serializer_class = UserUpdateSerializer
    queryset = BaseUser.objects.all()


class UserDeleteApi(APIView):
    permission_classes = [IsAdminOrOwner]
    serializer_class = UserDeleteSerializer
    
    def post(self, request, *args, **kwargs):
        user = user_get(user_id=kwargs['pk'])

        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserMeApi(generics.RetrieveAPIView):
    permission_classes = [IsBaseUser]
    queryset = BaseUser.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user