from django.core.management.base import BaseCommand
from apps.users.models import User
from django.conf import settings


class Command(BaseCommand):
    help = "Create default superuser from .env file"

    def handle(self, *args, **options):
        USERNAME = settings.ADMIN_USERNAME
        PASSWORD = settings.ADMIN_PASSWORD
        EMAIL = settings.ADMIN_EMAIL

        if not User.objects.filter(username=USERNAME, email=EMAIL).exists():
            try:
                user = User.objects.create_superuser(
                    username=USERNAME, password=PASSWORD, email=EMAIL
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Superuser {user.username} successfully created."
                    )
                )

            except Exception:
                self.stdout.write(
                    self.style.WARNING(f"Superuser {USERNAME} already exists.")
                )
        else:
            self.stdout.write(
                self.style.WARNING(f"Superuser {USERNAME} already exists.")
            )
