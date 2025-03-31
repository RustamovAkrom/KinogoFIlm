from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.genre import Genre


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
