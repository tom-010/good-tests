from django.test import TestCase
from infra.save_deep import save_deep
from desiderata.models import Desiderata
from django.shortcuts import reverse

class TestDesiderata(TestCase):
    
    def test_url_resolves(self):
        desiderata = save_deep(Desiderata.example())
        url = reverse('desiderata:detail', kwargs={'desiderata_slug': desiderata.slug})
        response = self.client.get(url)
        self.assertIsInstance(response.context['desiderata'], Desiderata)
        self.assertTemplateUsed(response, 'desiderata/detail.html')

    def test_desiderate_not_exists(self):
        url = reverse('desiderata:detail', kwargs={'desiderata_slug': 'non-existing'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)