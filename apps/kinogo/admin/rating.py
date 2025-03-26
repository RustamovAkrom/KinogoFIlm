from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.rating import MovieRating


@admin.register(MovieRating)
class MovieRatingAdmin(ModelAdmin):
    pass
