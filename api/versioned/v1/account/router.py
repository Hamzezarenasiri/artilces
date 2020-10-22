from rest_framework.routers import DefaultRouter

from . import views

ROUTER = DefaultRouter()
ROUTER.register("auth", views.AuthViewSet, basename="auth")
account_urlpatterns = ROUTER.urls
