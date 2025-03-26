from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models.base import AbstractBaseModel


class Actor(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name = _("Actor")
        verbose_name_plural = _("Actors")
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name