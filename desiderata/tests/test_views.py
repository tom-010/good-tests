from django.test import TestCase
from infra.save_deep import save_deep
from desiderata.models import Desiderata
from django.shortcuts import reverse

class TestDesiderata(TestCase):
    
    def test_url_resolves(self):
        desiderata = save_deep(Desiderata.example())
        url = f'/desideratas/detail/{desiderata.slug}'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'desiderata/detail.html')
        self.assertIsInstance(response.context['desiderata'], Desiderata)

    def test_desiderate_not_exists(self):
        url = reverse('desiderata:detail', kwargs={'desiderata_slug': 'non-existing'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

class TestDesiderataList(TestCase):

    def test_url_resolves(self):
        save_deep(Desiderata.example())
        save_deep(Desiderata.example())
        response = self.client.get(f'/desideratas/all')
        self.assertTemplateUsed(response, 'desiderata/all.html')
        desideratas = response.context['desideratas']
        self.assertEqual(2, len(desideratas))
        for desiderata in desideratas:
            self.assertIsInstance(desiderata, Desiderata)