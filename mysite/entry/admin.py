from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'text']
    search_fields = ['name']


admin.site.register(Note, NoteAdmin)




