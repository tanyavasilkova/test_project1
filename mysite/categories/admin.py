from django.contrib import admin
from . import models
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    class Meta:
        model = models.Category


admin.site.register(models.Category, CategoryAdmin)


