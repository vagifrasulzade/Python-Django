from rest_framework import viewsets
from .models import Category, Post, Book
from .serializers import CategorySerializer, PostSerializer, PostDetailSerializer, BookSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import PostPagination, CategoryPagination, BookPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["id", "name"]
    ordering = ["name"]

    permission_classes = [IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = PostPagination

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "title"]
    ordering = ["-created_at"]

    def get_serializer_class(self):
        if self.action in ["retrieve", "update", "partial_update"]:
            return PostDetailSerializer
        return PostSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "text"]
    ordering_fields = ["name", "price"]
    ordering = ["name"]

    permission_classes = [IsAuthenticatedOrReadOnly]


# www.domain/api/post/3
# www.domain/api/post > Get > Post











# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     pagination_class = PageNumberPagination

#     filter_backends = [SearchFilter]
#     search_fields = ["title", "content"]


# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
