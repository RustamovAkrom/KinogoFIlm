from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.shared.models.base import AbstractBaseModel


class WatchHistory(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="watch_histories")
    movie = models.ForeignKey("kinogo.Movie", on_delete=models.CASCADE, related_name="watch_histories")
    
    class Meta:
        unique_together = ('user', 'movie')
        verbose_name = _("Watch History")
        verbose_name_plural = _("Watch Histories")
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user} watched movie: {self.movie.title}"
