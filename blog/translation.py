from modeltranslation.translator import TranslationOptions, translator

from blog.models import City


class CityTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(City, CityTranslationOptions)
