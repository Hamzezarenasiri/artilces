from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class ArticleConfig(AppConfig):
    name = "apps.article"
    verbose_name = ugettext_lazy("Article")
