# encoding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    name = models.CharField(_('name'), max_length=230)
    email = models.EmailField(_('email address'))
    comment = models.CharField(_('Comment'), max_length=250, blank=True)

    def __unicode__(self):
        return "%s" % self.name

'''
class Technology(models.Model):
    title = models.CharField(_('name'), max_length=230)
    imgage = models.FileField(upload_to='technologies')

    def __unicode__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(_('name'), max_length=230)
    pub_date = models.DateField(verbose_name=_("Start Date"))
    description = models.TextField(verbose_name=_(u"Description"),
                                   null=True, blank=True)
    technologies = models.ManyToManyField(Technology)

    def __unicode__(self):
        return self.title
'''