from django.urls import resolve
from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'home.html')