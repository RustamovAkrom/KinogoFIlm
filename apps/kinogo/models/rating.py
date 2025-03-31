from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.shared.models.base import AbstractBaseModel


class MovieRating(AbstractBaseModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movie_ratings"
    )
    movie = models.ForeignKey(
        "kinogo.Movie", on_delete=models.CASCADE, related_name="movie_ratings"
    )
    rating = models.IntegerField(
        _("Rating"), default=0, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ("user", "movie")
        verbose_name = _("Movie Rating")
        verbose_name_plural = _("Movie Ratings")

    def __str__(self):
        return f"kino: {self.movie}, user: {self.user}: Rating - {self.rating}"
