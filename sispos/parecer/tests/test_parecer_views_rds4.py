from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.parecer.tests import mock


class Rds4ViewGetTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        self.resp = self.client.get(r('parecer:parecer_rds4_new',
                                      slug=str(relatorio.uuid)))

    def test_status_code(self):
        """Status code must be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render parecer_new.html template"""
        self.assertTemplateUsed(self.resp, 'parecer_new.html')

    def test_context_has_form(self):
        """Context must have a form"""
        context = self.resp.context
        self.assertIn('form', context)
