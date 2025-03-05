REST_AUTH = {
    "LOGIN_SERIALIZER": "features.authentication.serializers.CustomLoginSerializer",
    "USER_DETAILS_SERIALIZER": "features.users.serializers.UserDetailSerializer",
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "access-token",
    "JWT_AUTH_REFRESH_COOKIE": "refresh-token",
    "LOGOUT_ON_PASSWORD_CHANGE": True,

}