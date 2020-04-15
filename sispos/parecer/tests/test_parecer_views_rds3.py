from django.test import TestCase
from django.shortcuts import resolve_url as r


class Rds3ViewsGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('parecer:parecer_rds3_new'))

    def test_status_code(self):
        """Status code must be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render parecer_new.py"""
        self.assertTemplateUsed(self.resp, 'parecer_new.html')

