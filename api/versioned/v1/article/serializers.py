from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from apps.article.models import (
    Article,
)


class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source="author.get_full_name",
        label=_("author name"),
        help_text=_("author name display..."),
    )

    class Meta:
        model = Article
        fields = (
            "title",
            "author",
        )
        read_only_fields = fields


class ArticleDetailSerializer(ArticleListSerializer):
    class Meta(ArticleListSerializer.Meta):
        fields = (
            "title",
            "content",
            "created_time",
        )


class ArticleCreateSerializer(ArticleDetailSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta(ArticleDetailSerializer.Meta):
        fields = (
            "author",
            "title",
            "content",
        )
        read_only_fields = ("author",)
