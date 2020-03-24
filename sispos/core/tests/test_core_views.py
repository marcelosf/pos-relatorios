from django.test import TestCase
from django.shortcuts import resolve_url as r


class CoreViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render index.html template"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_base_template(self):
        """It should render base.html template"""
        self.assertTemplateUsed(self.resp, 'base.html')

    def test_bootstrap_scripts(self):
        scripts = ['bootstrap.min.css', 'bootstrap.min.js']

        for expected in scripts:
            with self.subTest():
                self.assertContains(self.resp, expected)
