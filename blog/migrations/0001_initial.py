# Generated by Django 3.2.5 on 2021-07-29 05:59

import ckeditor.fields
import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import location_field.models.plain
import stdimage.models
import taggit.managers
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0003_taggeditem_add_unique_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=55)),
                ("title_ru", models.CharField(max_length=55, null=True)),
                ("title_en", models.CharField(max_length=55, null=True)),
                ("timezone", timezone_field.fields.TimeZoneField(default="Europe/Moscow")),
                ("location", location_field.models.plain.PlainLocationField(max_length=63)),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("color", colorfield.fields.ColorField(default="#FF0000", max_length=18)),
                ("my_order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name_plural": "cities",
                "ordering": ["my_order"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", stdimage.models.StdImageField(blank=True, null=True, upload_to="post_images")),
                ("text", ckeditor.fields.RichTextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="posts", to=settings.AUTH_USER_MODEL
                    ),
                ),
                ("city", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="blog.city")),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
        ),
    ]