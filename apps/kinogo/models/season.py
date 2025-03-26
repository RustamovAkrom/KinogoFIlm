from django.utils.translation import gettext_lazy as _
from django.db import models


class Season(models.Model):
    poster = models.ImageField(_("Season poster"), upload_to="movies/seasons/%Y/%m/%d", blank=True, null=True)
    movie = models.ForeignKey("kinogo.Movie", on_delete=models.CASCADE, related_name="seasons")
    number = models.PositiveIntegerField(_("Season number"))
    title = models.CharField(_("Title"), max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('movie', 'number')
        verbose_name = _("Season")
        verbose_name_plural = _("Seasons")

    def __str__(self):
        return f"Season {self.number} - {self.movie.title}"
