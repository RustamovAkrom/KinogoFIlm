from django.db.models import Manager


class MovieManager(Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('category').prefetch_related('genres', 'actors')
