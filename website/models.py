# encoding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Contact(models.Model):
    name = models.CharField(_('name'), max_length=230)
    email = models.EmailField(_('email address'))
    comment = models.CharField(_('Comment'), max_length=250, blank=True)

    def __str__(self):
        return self.title