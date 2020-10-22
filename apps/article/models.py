from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from base_app.models.fields import (
    FarsiCharField,
    FarsiTextField,
)
from base_app.models.mixins import (
    BaseActiveModelMixin,
    TimestampedMixin,
)

USER_MODEL = get_user_model()


class Article(TimestampedMixin, BaseActiveModelMixin):
    author = models.ForeignKey(
        to=USER_MODEL,
        on_delete=models.CASCADE,
        related_name="article",
        verbose_name=_("author"),
    )
    title = FarsiCharField(verbose_name=_("title"), max_length=30)
    content = FarsiTextField(verbose_name=_("content"), max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
