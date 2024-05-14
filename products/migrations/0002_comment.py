# Generated by Django 4.2.11 on 2024-05-12 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField()),
                (
                    "stars",
                    models.CharField(
                        choices=[
                            ("1", "very bad"),
                            ("2", "bad"),
                            ("3", "normal"),
                            ("4", "good"),
                            ("5", "perfect"),
                        ],
                        max_length=10,
                    ),
                ),
                ("datetime_create", models.DateTimeField(auto_now_add=True)),
                ("datetime_modiefied", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
