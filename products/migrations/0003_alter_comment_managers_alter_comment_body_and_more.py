# Generated by Django 4.2.11 on 2024-05-15 10:58

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_comment"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="comment",
            managers=[
                ("active_comment_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=models.TextField(verbose_name="comment text"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="stars",
            field=models.CharField(
                choices=[
                    ("1", "very bad"),
                    ("2", "bad"),
                    ("3", "normal"),
                    ("4", "good"),
                    ("5", "perfect"),
                ],
                max_length=10,
                verbose_name=" your score?",
            ),
        ),
    ]