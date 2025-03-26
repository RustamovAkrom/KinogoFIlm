from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.season import Season


@admin.register(Season)
class SeasonAdmin(ModelAdmin):
    list_display = ("number", "title", "movie", "poster_preview", )
    list_filter = ("movie", )
    search_fields = ("title", "movie__title", )
    autocomplete_fields = ("movie", )

    def poster_preview(self, obj):
        if obj.poster:
            return f'<img src="{obj.poster.url}" width="50" height="75" style="object-fit: cover;" />'
        return "No poster"
    poster_preview.allow_tags = True
    poster_preview.short_description = "Poster"
