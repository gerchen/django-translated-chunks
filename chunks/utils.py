from django.db import models
from django.conf import settings
from django.utils.translation import get_language


class TranslatedModel(models.Model):

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(TranslatedModel, self).__init__(*args, **kwargs)
        self._language = getattr(settings, 'FORCE_MODEL_LANGUAGE', None) or get_language()
        self._translation_cache = {}

    def __getattr__(self, attr):
        if attr.startswith('translated'):
            attr = attr.split('_', 1)[1]
            translated_attrs = self.translations.model._meta.get_all_field_names()
            if attr in translated_attrs:
                if not self._translation_cache:
                    for trans in self.translations.select_related():
                        self._translation_cache[trans.language_code] = trans
                if self._language in self._translation_cache:
                    translated_attr = getattr(self._translation_cache[self._language], attr)
                    if translated_attr:
                        return translated_attr
                return getattr(self, attr)
        raise AttributeError


class TranslationModel(models.Model):

    class Meta:
        abstract = True

    language_code = models.CharField(
        _('Language'), max_length=7, choices=settings.LANGUAGES,
        blank=False, null=False)

    def __unicode__(self):
        return 'Translation to %s language' % self.language_code.upper()
