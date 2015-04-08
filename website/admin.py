# encoding: utf-8
from django.contrib import admin
from website.models import Contact, Technology, Project


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = (
        'name', 'email', 'comment')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Technology)
admin.site.register(Project)
