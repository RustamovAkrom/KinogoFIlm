from apps.shared.models.base import AbstractBaseModel
from django.db import models


class SiteStats(AbstractBaseModel):
    total_users = models.PositiveIntegerField(default=0)
    total_movies = models.PositiveIntegerField(default=0)
    total_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return (
            f"Total Users: {self.total_users}\n"
            f"Total Movies: {self.total_movies}\n"
            f"Total Views: {self.total_views}\n"
        )
