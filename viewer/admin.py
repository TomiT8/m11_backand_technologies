from django.contrib import admin
from django.contrib.admin import ModelAdmin

from viewer.models import *


class MovieAdmin(ModelAdmin):

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        for obj in queryset:
            obj.description = ""
            obj.save()

    ordering = ['title_orig', 'year']
    list_display = ['id', 'title_orig', 'title_cz', 'year']
    list_display_links = ['id', 'title_orig']
    list_per_page = 20
    list_filter = ['genres', 'countries']
    search_fields = ['title_orig', 'title_cz']
    actions = ['cleanup_description']

    fieldsets = [
        ('Title', {'fields': ['title_orig', 'title_cz']}),
        ('External Information', {'fields': ['genres', 'countries', 'year', 'length'], 'description': (
                    'These fields are going to be filled with data parsed '
                    'from external databases.'
                )}),
        ('Creators', {'fields': ['directors', 'actors'], 'description': 'These fields are intended to be filled in by our users.'}),
        ('User information', {'fields': ['description']}),
        ('Internal informations', {'fields': ['created', 'updated']})
    ]
    readonly_fields = ['created', 'updated']


admin.site.register(Country)
admin.site.register(Creator)
admin.site.register(Genre)
admin.site.register(Image)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
