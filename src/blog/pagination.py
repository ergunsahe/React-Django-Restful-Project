from rest_framework.pagination import PageNumberPagination


class BlogPostPagePagination(PageNumberPagination):
    page_size = 6