from django.test import TestCase

class TestHome(TestCase):

    def test_home_resolves(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')