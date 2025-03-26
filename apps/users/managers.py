from django.db.models import Manager


class UserManager(Manager):
    def active_users(self):
        """Активные пользователи с аватарками и профилем."""
        return self.select_related("profile").filter(is_active=True)

    def verified_users(self):
        """Проверенные пользователи."""
        return self.filter(is_verified=True)

    def with_full_data(self):
        """Оптимизированный запрос с профилем и аватаркой."""
        return self.select_related("profile").only("username", "email", "avatar", "profile__country")
