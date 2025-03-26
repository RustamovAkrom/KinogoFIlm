from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.actor import Actor


@admin.register(Actor)
class ActorAdmin(ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )