from django.test import TestCase
from django.shortcuts import resolve_url as r


class RelatoriosViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('relatorios:relatorios_new'))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render relatorios_novo.html"""
        self.assertTemplateUsed(self.resp, 'relatorios_novo.html')

    def test_base_template(self):
        """It should render base.html"""
        self.assertTemplateUsed(self.resp, 'base.html')
