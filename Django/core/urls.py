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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from article import views
# from article.views import articles__view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home__view),
    path("articles/", views.articles__view, name="articles"),
    path("article-detail/<int:id>", views.article__detail__view, name="article-detail"),
    path("article/create/", views.article_create__view, name="article-create"),
    path("article/<int:id>/edit/", views.article_edit__view, name="article-edit"),
    path("article/<int:id>/delete/", views.article_delete__view, name="article-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)