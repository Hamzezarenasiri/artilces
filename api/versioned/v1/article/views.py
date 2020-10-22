from rest_framework import (
    mixins,
    permissions,
    viewsets,
)

from apps.article.models import Article
from . import serializers


class ArticleViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (permissions.AllowAny,)
    serializer_classes = {
        "list": serializers.ArticleListSerializer,
        "retrieve": serializers.ArticleDetailSerializer,
        "create": serializers.ArticleCreateSerializer,
    }
    default_serializer_class = serializers.ArticleListSerializer
    permission_classes_by_action = {
        "create": (permissions.IsAuthenticated,),
        "retrieve": (permissions.AllowAny,),
        "list": (permissions.AllowAny,),
    }

    def get_queryset(self):
        return Article.active_objects.active()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
