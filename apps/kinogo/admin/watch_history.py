from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.watch_history import WatchHistory


@admin.register(WatchHistory)
class WatchHistoryAdmin(ModelAdmin):
    pass
