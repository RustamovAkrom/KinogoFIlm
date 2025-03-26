from django.utils.translation import gettext_lazy as _
from django.db import models



class Episode(models.Model):
    thumbnail = models.ImageField(_("Episode thumbnail"), upload_to="movies/episodes/%Y/%m/%d", blank=True, null=True)
    season = models.ForeignKey("kinogo.Season", on_delete=models.CASCADE, related_name="episodes")
    number = models.PositiveIntegerField(_("Episode number"))
    title = models.CharField(_("Title"), max_length=255, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    duration = models.DurationField(_("Duration"))
    video_file = models.FileField(_("Episode file"), upload_to="movies/episodes/%Y/%m/%d")
    release_date = models.DateField(_("Release date"), blank=True, null=True)
    alt_sources = models.JSONField(_("Alternative sources"), blank=True, null=True)
    
    class Meta:
        unique_together = ('season', 'number')
        verbose_name = _("Episode")
        verbose_name_plural = _("Episodes")
    
    def __str__(self):
        return f"Episode {self.number} - {self.season.movie.title}"
    