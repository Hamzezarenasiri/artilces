# Generated by Django 3.1.2 on 2020-10-22 13:21

import base_app.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        help_text="Designates whether this item should be treated as active. Unselected this instead of deleting.",
                        verbose_name="Active status",
                    ),
                ),
                (
                    "created_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creation On"),
                ),
                (
                    "updated_time",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="Modified On"
                    ),
                ),
                (
                    "title",
                    base_app.models.fields.FarsiCharField(
                        max_length=30, verbose_name="title"
                    ),
                ),
                (
                    "content",
                    base_app.models.fields.FarsiTextField(
                        max_length=1000, verbose_name="title"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="article",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="author",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
            managers=[
                ("active_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
