from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from taggit_helpers.admin import TaggitCounter, TaggitStackedInline

from blog.models import City, Post


class PostAdmin(TaggitCounter, admin.ModelAdmin):
    list_display = (
        "__str__",
        "taggit_counter",
    )
    inlines = [TaggitStackedInline]


class CityAdmin(SortableAdminMixin, TranslationAdmin, admin.ModelAdmin):
    list_display = ("__str__", "flag")

    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


admin.site.register(Post, PostAdmin)
admin.site.register(City, CityAdmin)
