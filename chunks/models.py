from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils import TranslatedModel, TranslationModel


class Chunk(TranslatedModel):
    """
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(_(u'Key'),
        help_text=_(u"A unique name for this chunk, "
                     "slug which is used in template"),
        blank=False, max_length=255, unique=True)
    page = models.CharField(_(u'Page'),
        help_text=_(u"Page of the chunk, used for sorting "
                     "and filtering list of chunks in admin"),
        blank=True, max_length=255)
    content = models.TextField(_(u'Content'), blank=True)
    description = models.CharField(_(u'Description'), blank=True, max_length=64,
        help_text=_(u"Short Description"))

    class Meta:
        ordering = ['key']
        verbose_name = _(u'chunk')
        verbose_name_plural = _(u'chunks')

    def __unicode__(self):
        return u"%s" % (self.key,)


class ChunkTranslation(TranslationModel):
    parent = models.ForeignKey(Chunk, related_name='translations')
    content = models.TextField(_(u'Content'), blank=True)
    description = models.CharField(_(u'Description'), blank=True,
        max_length=64, help_text=_(u"Short Description"))
