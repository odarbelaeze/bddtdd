from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeViewTest(TestCase):

    def test_uses_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'taskbuster/index.html')

    def test_uses_base_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base.html')
