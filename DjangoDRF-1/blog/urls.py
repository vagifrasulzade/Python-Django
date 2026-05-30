from django.urls import path
from . import views_fbv, views_cbv, views_generic

# MƏRHƏLƏ 1 — @api_view (FBV)
# urlpatterns = [
#     path('posts/', views_fbv.post_list),
#     path('posts/<int:pk>/', views_fbv.post_detail),
# ]

# MƏRHƏLƏ 2 — APIView (CBV)
urlpatterns = [
    path('posts/', views_cbv.PostListAPIView.as_view()),
    path('posts/<int:pk>/', views_cbv.PostDetailAPIView.as_view()),
    path('posts/<int:post_pk>/comments/', views_cbv.CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', views_cbv.CommentDetailAPIView.as_view()),
]

# MƏRHƏLƏ 3 — Generic Views (final)
# urlpatterns = [
#     path('categories/', views_generic.CategoryListCreateView.as_view()),
#     path('posts/', views_generic.PostListCreateView.as_view()),
#     path('posts/<int:pk>/', views_generic.PostDetailView.as_view()),
# ]

