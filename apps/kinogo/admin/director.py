from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.director import Director


@admin.register(Director)
class DirectorAdmin(ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )