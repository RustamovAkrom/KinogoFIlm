from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User, UserProfile

from unfold.admin import ModelAdmin, StackedInline
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm


class UserProfileInline(StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    change_password_form = AdminPasswordChangeForm
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = (
        "id",
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_verified",
        "is_social_user",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)
    list_editable = ("is_active", "is_staff", "is_superuser")
    filter_vertical = ("groups", "user_permissions")
    inlines = (UserProfileInline,)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
