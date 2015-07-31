from django.contrib import admin
from resources.models import Resource, Type


# Register your models here.
class ResourceAdmin(admin.ModelAdmin):
    model = Resource
    search_fields = ['title', 'url']
    ordering = ['-created', '-title']
    list_display = (
        'created', 'title', 'url', 'comment')


admin.site.register(Resource, ResourceAdmin)
admin.site.register(Type)