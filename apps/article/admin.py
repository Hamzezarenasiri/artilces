from django.contrib import admin

from .models import (
    Article,
)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
        "content",
        "is_active",
        "created_time",
        "updated_time",
    )
    list_filter = ("is_active", "created_time", "updated_time", "author")
