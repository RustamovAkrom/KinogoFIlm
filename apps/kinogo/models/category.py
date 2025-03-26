from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models.base import AbstractBaseModel


class Category(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    