from rest_framework import pagination


class BasePageNumberPagination(pagination.PageNumberPagination):
    page_query_param = "p"
    page_size_query_param = "ps"
    page_size = 20
    max_page_size = 50


class UnlimitedPageNumberPagination(pagination.PageNumberPagination):
    page_query_param = "p"
    page_size_query_param = "ps"
    page_size = 100
    max_page_size = 50


class BaseLimitOffsetPagination(pagination.LimitOffsetPagination):
    max_limit = 200
