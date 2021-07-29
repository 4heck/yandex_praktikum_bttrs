import datetime

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from location_field.models.plain import PlainLocationField
from loguru import logger
from stdimage import StdImageField
from taggit.managers import TaggableManager
from timezone_field import TimeZoneField

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = StdImageField(
        upload_to="post_images",
        variations={"thumbnail": {"width": 100, "height": 75}},
        null=True,
        blank=True,
    )
    text = RichTextField()
    tags = TaggableManager()
    city = models.ForeignKey("City", on_delete=models.CASCADE)

    def __str__(self):
        return f"Post #{self.pk}"

    def save(self, *args, **kwargs):
        logger.debug(f"You have saved the post #{self.pk} at {datetime.datetime.now()}")
        super(Post, self).save(*args, **kwargs)


class City(models.Model):
    title = models.CharField(max_length=55)
    timezone = TimeZoneField(default="Europe/Moscow")
    location = PlainLocationField(based_fields=["title"], zoom=7)
    country = CountryField()
    color = ColorField(default="#FF0000")
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    @property
    def flag(self):
        return mark_safe(f'<img src="{self.country.flag}" width="15" height="15" />')

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name_plural = "cities"
        ordering = ["my_order"]
