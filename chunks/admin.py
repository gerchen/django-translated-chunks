from django.contrib import admin
from django.db.models import TextField
from models import Chunk, ChunkTranslation
from django_summernote.widgets import SummernoteWidget


class ChunkTranslationInline(admin.StackedInline):
    formfield_overrides = {
        TextField: {'widget': SummernoteWidget}
    }
    model = ChunkTranslation
    extra = 1


class ChunkAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': SummernoteWidget}
    }
    list_display = ('key', 'page', 'description',)
    search_fields = ('key', 'content')
    list_filter = ('page', )
    inlines = [
        ChunkTranslationInline
    ]


admin.site.register(Chunk, ChunkAdmin)
