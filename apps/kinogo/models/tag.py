from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models.base import AbstractBaseModel


class Tag(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    

class MovieTag(models.Model):
    movie = models.ForeignKey("kinogo.Movie", on_delete=models.CASCADE, related_name="movie_tags")
    tag = models.ForeignKey("kinogo.Tag", on_delete=models.CASCADE, related_name="movie_tags")


    class Meta:
        verbose_name = _("Movie Tag")
        verbose_name_plural = _("Movie Tags")
    
    def __str__(self):
        return self.tag.name
