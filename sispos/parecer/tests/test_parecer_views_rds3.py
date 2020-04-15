from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.parecer.tests import mock


class Rds3ViewsGetTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        self.client.force_login(relator)
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        self.resp = self.client.get(r('parecer:parecer_rds3_new',
                                      slug=str(relatorio.uuid)))

    def test_status_code(self):
        """Status code must be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render parecer_new.py"""
        self.assertTemplateUsed(self.resp, 'parecer_new.html')

    def test_context_form(self):
        """Context must contain form"""
        context = self.resp.context
        self.assertIn('form', context)
