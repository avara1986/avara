"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from website.models import Contact


class avaraTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_200(self):
        index_res = self.client.get(reverse('index_homepage'))
        self.assertEqual(index_res.status_code, 200)

    def test_post_forms_contact(self):
        contact_url = reverse('contact')
        contact_res = self.client.post(contact_url, {'name': 'Alberto',
                                                     'email': 'a.vara.1986@gmail.com',
                                                     'comment': 'Pruba'})
        self.assertEqual(contact_res.status_code, 302)
