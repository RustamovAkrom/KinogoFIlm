from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.kinogo.models.category import Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
