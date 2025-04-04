# Generated by Django 5.0.8 on 2025-03-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kinogo", "0003_rename_director_movie_directors_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="kinogo.actor"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="country",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Country"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="directors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="kinogo.director"
            ),
        ),
    ]
