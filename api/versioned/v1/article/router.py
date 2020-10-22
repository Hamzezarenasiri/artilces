from rest_framework.routers import DefaultRouter

from . import views

ROUTER = DefaultRouter()
ROUTER.register("", views.ArticleViewSet, basename="articles")
article_urlpatterns = ROUTER.urls
