# from django.urls import path
# from . import views

# urlpatterns = [
#     path('categories/', views.CategoryListCreateView.as_view()),
#     path('posts/', views.PostListCreateView.as_view()),
#     path('posts/<int:pk>/', views.PostDetailView.as_view()),
# ]

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("categories", views.CategoryViewSet)
router.register("posts", views.PostViewSet)
router.register("books", views.BookViewSet)
urlpatterns = router.urls