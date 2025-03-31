from django.db.models import TextChoices


class MovieTypeChoices(TextChoices):
    MOVIE = "movie", "Movie"
    SERIES = "series", "Series"
    MINI_SERIES = "mini_series", "Mini Series"
    DOCUMENTARY = "documentary", "Documentary"
