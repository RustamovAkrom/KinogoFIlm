from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.tag import Tag


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
