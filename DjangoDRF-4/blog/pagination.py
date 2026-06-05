from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param="page_size"
    max_page_size = 20


class CategoryPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 20


class BookPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 20