from django.test import TestCase
from django.shortcuts import resolve_url as r


class ParecerViewsGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('parecer:parecer_new'))

    def test_status_code(self):
        """Sttatus code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render parecer_ds1_new.html template"""
        self.assertTemplateUsed(self.resp, 'parecer_ds1_new.html')

    def test_extends_template(self):
        """It should extends base.html"""
        self.assertTemplateUsed(self.resp, 'base.html')
