# encoding: utf-8
from django.contrib import admin
from website.models import Contact, Technology, Project

admin.site.register(Contact)
admin.site.register(Technology)
admin.site.register(Project)