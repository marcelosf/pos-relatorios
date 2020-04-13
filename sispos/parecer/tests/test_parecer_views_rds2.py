from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.parecer.tests import mock


class ViewsPrecerGetTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        self.relatorio = mock_relatorio.save_relatorio(relatorio_data)
        self.resp = self.client.get(r('parecer:parecer_rds2_new',
                                    slug=str(self.relatorio.uuid)))

    def test_status_code(self):
        """Status code must be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It must render parecer_new.html"""
        self.assertTemplateUsed(self.resp, 'parecer_new.html')

    def test_context_params(self):
        """Context must contain params"""
        params = ['slug', 'form', 'action']
        for expected in params:
            with self.subTest():
                self.assertIn(expected, self.resp.context)

    def test_action_url(self):
        """It must contain the action url"""
        expected = 'action="{}"'.format(r('parecer:parecer_rds2_new',
                                          slug=str(self.relatorio.uuid)))
        self.assertContains(self.resp, expected)