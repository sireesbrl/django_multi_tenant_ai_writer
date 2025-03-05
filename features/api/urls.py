from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("users/", include("features.users.urls")),
    path("auth/", include("features.authentication.urls"), name="auth"),
    # For browsable API
    path("rest-browsable-auth/", include("rest_framework.urls")),
]
