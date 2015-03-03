# encoding: utf-8
from django import forms
from website.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact