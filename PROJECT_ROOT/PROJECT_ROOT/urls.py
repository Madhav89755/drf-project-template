from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView

admin.site.site_title = "Admin"
admin.site.site_header = "Administrator"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/token/", TokenObtainPairView.as_view()),

    path('api/schema/', SpectacularAPIView.as_view(),
         name='schema'),  # Swagger Documentation File
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # Redoc UI
] + debug_toolbar_urls()
