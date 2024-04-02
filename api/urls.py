"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from api.moods import views as mood_views
from . import views as api_views

router = DefaultRouter()
router.register(r'moods', mood_views.MoodLogViewSet)

urlpatterns = [
    # auto CRUD for registered models
    path('', include(router.urls)),

    # djnago admin site
    path('admin/', admin.site.urls),

    # OpenAPI and swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

    # local auth for testing
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # auth for front end
    path('login', api_views.login),
    path('signup', api_views.signup),
    path('test_token', api_views.test_token)
]
