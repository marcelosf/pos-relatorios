from django.test import TestCase
from django.shortcuts import resolve_url as r


class CoreViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)
