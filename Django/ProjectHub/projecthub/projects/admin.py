from django.contrib import admin
from .models import Projects, Tag

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    # fields = ('title', 'tags', 'created')
    date_hierarchy = 'created'
    search_fields = ['title', 'description', 'tags__name']
    list_editable = ['demo_link', 'source_link', 'project_priority_sl']
    list_display_links = ['title']
    list_display = ('title', 'search_tags', 'demo_link',
                    'source_link', 'project_priority_sl')

    def search_tags(self, obj):
        return ", ".join([t.name for t in obj.tags.all()])


class TagAdmin(admin.ModelAdmin):
    # fields = ('title', 'tags', 'created')
    date_hierarchy = 'created'
    search_fields = ['name']
    # list_display = ('name')


admin.site.register(Projects, ProjectAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.site_header = 'ProjectHub Admin Dashboard'
admin.site.site_title = 'ProjectHub | All Projects in One Place!'
