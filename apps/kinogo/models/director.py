from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models.base import AbstractBaseModel


class Director(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name = _("Director")
        verbose_name_plural = _("Directors")
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
