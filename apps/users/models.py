from datetime import datetime

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken

from apps.shared.models.base import AbstractBaseModel
from .managers import UserManager # noqa


class User(AbstractUser):
    email = models.EmailField(_("Email"), unique=True)
    avatar = models.ImageField(_("Avatar"), upload_to="users/avatars/%Y/%m/%d", null=True, blank=True)
    bio = models.TextField(_("Bio"), blank=True)
    is_verified = models.BooleanField(_("Verified"), default=True)
    date_of_birth = models.DateTimeField(_("Date of birth"), null=True, blank=True)
    is_social_user = models.BooleanField(_("Is social user"), default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        ts = refresh.access_token.payload['exp']
        dt = datetime.fromtimestamp(ts)
        data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'expires_in': str(dt),
            'user_id': str(self.id),
        }
        return data
    
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
        return self.get_full_name_or_username()
    

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