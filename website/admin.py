# encoding: utf-8
from django.contrib import admin
from website.models import Contact, Resource, Type


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = (
        'created', 'name', 'email', 'comment')


class ResourceAdmin(admin.ModelAdmin):
    model = Contact
    search_fields = ['title', 'url']
    list_filter = ('types',)
    ordering = ['-created', '-title']
    list_display = (
        'created', 'title', 'url', 'comment')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Type)
