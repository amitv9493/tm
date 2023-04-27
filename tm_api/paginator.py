from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_query_param='p'
    page_size_query_param = 'records'