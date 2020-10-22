"""
set of custom models to use in apps
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .manager import ActiveModelManager


class BaseActiveModelMixin(models.Model):
    """
    a abstract model - it's preferred for all models to inheritance from this model
    """

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active status"),
        db_index=True,
        help_text=_(
            "Designates whether this item should be treated as active. "
            "Unselected this instead of deleting."
        ),
    )

    active_objects = ActiveModelManager()
    objects = models.Manager()

    class Meta:
        abstract = True


class TimestampedMixin(models.Model):
    # A timestamp representing when this object was created.
    created_time = models.DateTimeField(
        verbose_name=_("Creation On"), auto_now_add=True
    )
    # A timestamp reprensenting when this object was last updated.
    updated_time = models.DateTimeField(
        verbose_name=_("Modified On"), auto_now=True, db_index=True
    )

    class Meta:
        abstract = True
        ordering = ["-created_time", "-updated_time"]
