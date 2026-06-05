"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from users.views import LogoutApiView, RegisterApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

     # 1. Qeydiyyat (Bizim yazdığımız)
    path('api/auth/register/', RegisterApiView.as_view(), name='auth_register'),
    # 2. Giriş / Login (Kitabxananın hazır verdiyi - Access və Refresh Token qaytarır)
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 3. Token Yeniləmə (Kitabxananın hazır verdiyi - Yeni Access Token qaytarır)
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 4. Çıxış / Logout (Bizim yazdığımız)
    path('api/auth/logout/', LogoutApiView.as_view(), name='auth_logout'),
]
