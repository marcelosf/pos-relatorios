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


class Rds3ViewsPostTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        self.client.force_login(relator)
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        mock_rds3 = mock.MockParecer()
        rds3_data = mock_rds3.make_rds3(relatorio=relatorio, relator=relator)
        self.resp = self.client.post(r('parecer:parecer_rds3_new',
                                       slug=str(relatorio.uuid)), rds3_data)

    def test_status_code(self):
        """Status code must be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_form_is_valid(self):
        """form must be valid"""
        form = self.resp.context['form']
        self.assertTrue(form.is_valid())

    def test_message_success(self):
        """It must show a success message"""
        expected = 'Parecer enviado com sucesso.'
        self.assertContains(self.resp, expected)


class Rds3ViewsInvalidPostTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        self.client.force_login(relator)
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        self.resp = self.client.post(r('parecer:parecer_rds3_new',
                                       slug=str(relatorio.uuid)), {})

    def test_form_invalid(self):
        """Form must be invalid"""
        form = self.resp.context['form']
        self.assertFalse(form.is_valid())
