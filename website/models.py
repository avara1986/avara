# encoding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(_('name'), max_length=230)
    email = models.EmailField(_('email address'))
    comment = models.CharField(_('Comment'), max_length=250, blank=True)

    def __unicode__(self):
        return "%s" % self.name