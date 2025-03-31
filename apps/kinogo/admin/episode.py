from django.utils.html import format_html
from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.episode import Episode


@admin.register(Episode)
class EpisodeAdmin(ModelAdmin):
    list_display = (
        "number",
        "title",
        "season",
        "duration",
        "release_date",
    )
    list_filter = (
        "season",
        "release_date",
    )
    search_fields = (
        "title",
        "description",
        "season__movie__title",
    )
    autocomplete_fields = ("season",)
    readonly_fields = ("duration",)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("season", "season__movie")

    def movie_title(self, obj):
        return obj.season.movie.title

    movie_title.short_description = "Movie"

    def episode_display(self, obj):
        return f"S{obj.season.number:02}E{obj.number:02}"

    episode_display.short_description = "Episode"

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    # Добавляем предпросмотр видео
    def video_preview(self, obj):
        if obj.video_file:
            return format_html(
                '<video width="320" height="180" controls>'
                '<source src="{}" type="video/mp4">'
                "Your browser does not support the video tag."
                "</video>",
                obj.video_file.url,
            )
        return "No video"

    video_preview.short_description = "Preview"
