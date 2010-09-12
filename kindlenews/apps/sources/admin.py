from django.contrib import admin

from kindlenews.apps.sources.models import NewsSource


class SourceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic', {
            'fields': ('name', 'name_verbose', 'url', 'max_items')
        }),
        ('Selectors', {
            'fields': ('sel_stories', 'sel_title', 'sel_teaser', 'sel_link',
            	'sel_content', 'sel_continuations')
        }),
    )
    
admin.site.register(NewsSource, SourceAdmin)
