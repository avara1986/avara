from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangae import fields


# Create your models here.
class Type(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(_('name'), max_length=230)
    tag = models.CharField(_('name'), max_length=230)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        db_table = 'website_type'


class Resource(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(_('title'), max_length=230)
    url = models.CharField(_('Resource URL'), max_length=230)
    types = fields.RelatedSetField('Type')
    comment = models.TextField(_('Comment'), max_length=250, blank=True)

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        db_table = 'website_resource'
