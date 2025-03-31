from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db import models

from apps.shared.models.base import AbstractBaseModel
from apps.kinogo.managers.movie import MovieManager
from apps.kinogo.choices.movie import MovieTypeChoices
from .actor import Actor
from .director import Director
from .genre import Genre
from .category import Category


def validate_year(value):
    if value < 1900 or value > 2100:
        raise ValidationError("Год выпуска должен быть от 1900 до 2100!")


class Movie(AbstractBaseModel):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    banner = models.ImageField(_("Banner"), upload_to="movies/%Y/%m/%d")
    video_file = models.FileField(_("Movie"), upload_to="movies/%Y/%m/%d")
    trailer_url = models.URLField(_("Trailer URL"), blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    year_of_release = models.IntegerField(
        _("Year of relase"), blank=True, null=True, validators=[validate_year]
    )
    world_premiere = models.DateField(blank=True, null=True)
    country = models.CharField(_("Country"), max_length=100, blank=True, null=True)
    views_count = models.PositiveIntegerField(_("Views count"), default=0)
    duration = models.DurationField(_("Duration"), blank=True, null=True)
    language = models.CharField(_("Language"), max_length=50, blank=True, null=True)
    subtitles = models.JSONField(_("Subtitles"), blank=True, null=True)

    movie_type = models.CharField(
        _("Type"),
        max_length=20,
        choices=MovieTypeChoices.choices,
        default=MovieTypeChoices.MOVIE.value,
    )
    genres = models.ManyToManyField(Genre, related_name="movies")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    directors = models.ManyToManyField(Director, related_name="movies", blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)

    is_published = models.BooleanField(default=False)

    objects = MovieManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Movie.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=["views_count"])

    def calculate_rating(self):
        likes = self.movie_likes.count()
        dislikes = self.movie_dislikes.count()
        return likes - dislikes

    def is_popular(self):
        return self.views_count >= 10000

    def get_trailer_link(self):
        return self.trailer_url if self.trailer_url else "Trailer url not found!"

    def get_similar_movies(self):
        """Find similar movies by genre and category."""
        return (
            Movie.objects.filter(genre__in=self.genre.all())
            .exclude(id=self.id)
            .distinct()[:5]
        )

    def has_subtitles(self):
        return bool(self.subtitles)

    def get_duration_in_minutes(self):
        if self.duration:
            return int(self.duration.total_seconds() // 60)
        return None

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.year_of_release})"


class MovieLikes(AbstractBaseModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="movie_likes")
    movie = models.ForeignKey(
        "kinogo.Movie", models.CASCADE, related_name="movie_likes"
    )

    class Meta:
        verbose_name = _("Movie Like")
        verbose_name_plural = _("Movie Likes")
        ordering = ["-created_at"]
        unique_together = ("user", "movie")

    def __str__(self):
        return f"{self.user} liked {self.movies}"


class MovieDislikes(AbstractBaseModel):
    user = models.ForeignKey(
        "users.User", models.CASCADE, related_name="movie_dislikes"
    )
    movie = models.ForeignKey(
        "kinogo.Movie", models.CASCADE, related_name="movie_dislikes"
    )

    class Meta:
        verbose_name = _("Movie Like")
        verbose_name_plural = _("Movie Dislikes")
        ordering = ["-created_at"]
        unique_together = ("user", "movie")

    def __str__(self):
        return f"{self.user} liked {self.movies}"


class MovieComment(AbstractBaseModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movie_comments"
    )
    movie = models.ForeignKey(
        "kinogo.Movie", on_delete=models.CASCADE, related_name="movie_comments"
    )
    message = models.TextField(_("Message"))

    class Meta:
        verbose_name = _("Movie Comment")
        verbose_name_plural = _("Movie Comments")
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment from {self.user} on {self.movie.title}"
