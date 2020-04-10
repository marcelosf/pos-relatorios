from django.test import TestCase
from django.shortcuts import resolve_url as r


class ParecerViewsGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('parecer:parecer_new'))

    def test_status_code(self):
        """Sttatus code should be 200"""
        self.assertEqual(200, self.resp.status_code)
