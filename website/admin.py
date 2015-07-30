# encoding: utf-8
from django.contrib import admin
from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = (
        'created', 'name', 'email', 'comment')



admin.site.register(Contact, ContactAdmin)

