from django.urls import path
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)

urlpatterns = [
    path("jwt/password/reset/confirm/<str:uidb64>/<str:token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("jwt/login/", LoginView.as_view(), name="login"),
    path("jwt/logout/", LogoutView.as_view(), name="logout"),
    path("jwt/password/change/", PasswordChangeView.as_view(), name="password-change"),
    path("jwt/password/reset/", PasswordResetView.as_view(), name="password-reset"),
]
