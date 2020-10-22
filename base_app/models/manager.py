from django.db import models

from .query import (
    ActiveQuerySet,
)


class ActiveModelManager(models.Manager):
    """
    ActiveModelManager

    Manager to return instances of ActivatorModel: SomeModel.active_objects.active() / .inactive()
    """

    def get_queryset(self):
        """ Use ActiveQuerySet for all results """
        return ActiveQuerySet(model=self.model, using=self._db)

    def active(self):
        """
        Return active instances of BaseActiveModelMixin:

        SomeModel.active_objects.active(), proxy to ActiveQuerySet.active
        """
        return self.get_queryset().active()

    def inactive(self):
        """
        Return inactive instances of BaseActiveModelMixin:

        SomeModel.active_objects.inactive(), proxy to ActiveQuerySet.inactive
        """
        return self.get_queryset().inactive()
