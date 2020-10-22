"""
V1 api routers
"""
from django.urls import (
    include,
    path,
)
from rest_framework import routers

from .account.router import account_urlpatterns
from .article.router import article_urlpatterns

ROUTER = routers.DefaultRouter()
urlpatterns = [
    path("article/", include(article_urlpatterns)),
    path("account/", include(account_urlpatterns)),
]
urlpatterns += ROUTER.urls
