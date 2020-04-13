from django.test import TestCase
from django.shortcuts import resolve_url as r


class ViewsPrecerGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('parecer:parecer_rds2_new'))

    def test_status_code(self):
        """Status code must be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It must render parecer_rds2_new.html"""
        self.assertTemplateUsed(self.resp, 'parecer_ds1_new.html')
