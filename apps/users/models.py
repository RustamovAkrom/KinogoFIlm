from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.shared.models.base import AbstractBaseModel
from .managers import UserManager # noqa


class User(AbstractUser):
    email = models.EmailField(_("Email"), unique=True)
    avatar = models.ImageField(upload_to="users/avatars/%Y/%m/%d", null=True, blank=True)
    bio = models.TextField(blank=True)
    is_verified = models.BooleanField(_("Verified"), default=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)

    
    # Дополнительные методы
    def get_avatar_url(self):
        """Возвращает ссылку на аватар пользователя или дефолтный аватар."""
        return self.avatar.url if self.avatar else "/static/default_avatar.jpg"

    def get_full_name_or_username(self):
        """Если нет имени — вернуть юзернейм."""
        return f"{self.first_name} {self.last_name}" if self.first_name else self.username

    def is_adult(self):
        """Проверяет, совершеннолетний ли пользователь (18+)."""
        from datetime import date
        if self.date_of_birth:
            age = (date.today() - self.date_of_birth).days // 365
            return age >= 18
        return False

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
    

class UserProfile(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profiles")
    country = models.CharField(_("Country"), max_length=100, blank=True, null=True)
    city = models.CharField(_("City"), max_length=100, blank=True, null=True)
    website = models.URLField(_("Website"), blank=True, null=True)
    phone_number = models.CharField(_("Phone Number"), max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")