from django.utils.html import format_html
from django.contrib import admin

from unfold.admin import ModelAdmin, TabularInline

from apps.kinogo.models.movie import Movie, MovieLikes, MovieDislikes, MovieComment
from apps.kinogo.models.tag import MovieTag


class MovieTagInline(TabularInline):
    model = MovieTag
    extra = 1
    autocomplete_fields = ("tag", )


@admin.register(Movie)
class MovieAdmin(ModelAdmin):
    list_display = ("title", "year_of_release", "views_count", "is_published", )
    list_editable = ("is_published",)
    list_filter = ("year_of_release", "genres", "category", "is_published", )
    search_fields = ("title", "description", )
    autocomplete_fields = ("genres", "category", "directors", "actors", )
    readonly_fields = ("views_count", "slug", "movie_preview", "trailer_preview", )
    inlines = [MovieTagInline]
    fieldsets = (
        ("Основная информация", {"fields": ("title", "slug", "description", "year_of_release", "world_premiere", "country")}),
        ("Медиа", {"fields": ("banner", "video_file", "trailer_url", "movie_preview", "trailer_preview", )}),
        ("Дополнительные параметры", {"fields": ("duration", "language", "subtitles", "is_published")}),
        ("Категории и связи", {"fields": ("genres", "category", "directors", "actors")}),
        ("Системные данные", {"fields": ("views_count", )}),
    )
    def get_queryset(self, request):
        return super().get_queryset(request).select_related("category")

    # Предпросмотр трейлера
    def trailer_preview(self, obj):
        if obj.trailer_url:
            if "youtube.com" in obj.trailer_url or "youtu.be" in obj.trailer_url:
                if "youtu.be" in obj.trailer_url:
                    video_id = obj.trailer_url.split("/")[-1]
                else:
                    video_id = obj.trailer_url.split("v=")[-1].split("&")[0]

                embed_url = f"https://www.youtube.com/embed/{video_id}"

                # Встраиваем iframe с обработкой ошибки + ссылка "Посмотреть на YouTube"
                return format_html(
                    """
                    <iframe width="320" height="180" src="{}" frameborder="0" allowfullscreen></iframe>
                    <br>
                    <a href='{}' target='_blank' style='color: blue;'>Посмотреть на YouTube</a>
                    """,
                    embed_url,
                    obj.trailer_url
                )

            return "Invalid YouTube link"

        return "No trailer available"

    
    trailer_preview.short_description = "Trailer Preview"

    # Предпросмотр фильма в админке
    def movie_preview(self, obj):
        if obj.video_file:
            return format_html(
                '<video width="640" height="360" controls>'
                '<source src="{}" type="video/mp4">'
                'Your browser does not support the video tag.'
                '</video>',
                obj.video_file.url
            )
        return "No movie file available"
    
    movie_preview.short_description = "Movie Preview"


@admin.register(MovieLikes)
class MovieLikesAdmin(ModelAdmin):
    list_display = ("user", "movie", "created_at", )
    search_fields = ("user__username", "movie__title", )


@admin.register(MovieDislikes)
class MovieDislikesAdmin(ModelAdmin):
    list_display = ("user", "movie", "created_at", )
    search_fields = ("user__username", "movie__title", )


@admin.register(MovieComment)
class MovieCommentAdmin(ModelAdmin):
    list_display = ("user", "movie", "created_at", "message", )
    search_fields = ("user__username", "movie__title", "message", )
    list_filter = ("created_at", )
