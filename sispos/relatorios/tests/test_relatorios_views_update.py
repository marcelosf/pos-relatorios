from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.core import mail
from sispos.relatorios.models import Relatorios
from sispos.relatorios.tests import mock


class UpdateRelatorioTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        coordenador = mock_user.make_coordenador()
        self.client.force_login(coordenador)
        mock_relatorio = mock.MockRelatorio()
        self.relatorio_data = mock_relatorio.make_relatorio()
        self.relatorio = mock_relatorio.save_relatorio(self.relatorio_data)
        self.resp = self.client.get(r('relatorios:relatorios_update',
                                    slug=str(self.relatorio.uuid)))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render the relatorios_update.html"""
        self.assertTemplateUsed(self.resp, 'relatorios_update.html')

    def test_template_base(self):
        """It should render the base.html template"""
        self.assertTemplateUsed(self.resp, 'base.html')

    def test_context(self):
        """Context should contain an instance of Relatorios"""
        obj = self.resp.context['relatorio']
        self.assertIsInstance(obj, Relatorios)

    def test_title(self):
        """Template title should be rendered"""
        expected = 'Relatório de {}'.format(self.relatorio.nome)
        self.assertContains(self.resp, expected)

    def test_relatorio_data(self):
        """Template should render the relatorio data"""
        data = list(self.relatorio_data.values())[:3]
        data.append(self.relatorio.relatorio.url)
        data.append(self.relatorio.encaminhamento.url)
        for expected in data:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_has_form(self):
        """Template ahould have a form"""
        content = ['<form', 'method="post"']
        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context_has_form(self):
        """Context should have coordenador_form"""
        context = self.resp.context
        self.assertIn('form', context)

    def test_has_csrf_token(self):
        """It should render the csrf token"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_submit_button(self):
        """It should render a submit button"""
        expected = 'type="submit"'
        self.assertContains(self.resp, expected)

    def test_form_action(self):
        """form action should be /relatorios/update/"""
        expected = 'relatorios/update/{}'.format(str(self.relatorio.uuid))
        self.assertContains(self.resp, expected)


class UpdateRelatoriosLoggedOutTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        self.relatorio_data = mock_relatorio.make_relatorio()
        self.relatorio = mock_relatorio.save_relatorio(self.relatorio_data)
        self.resp = self.client.get(r('relatorios:relatorios_update',
                                    slug=str(self.relatorio.uuid)))

    def test_redirect_logged_out_user(self):
        """Status code should be 302"""
        self.assertEqual(302, self.resp.status_code)


class UpdateRelatorioPostTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        mock_user = mock.MockUser()
        coordenador = mock_user.make_coordenador()
        self.client.force_login(coordenador)
        relator = mock_user.make_relator()
        mail.outbox = []
        self.resp = self.client.post(r('relatorios:relatorios_update',
                                       slug=str(relatorio.uuid)),
                                     {'relator': relator.pk})

    def test_relatorio_updated(self):
        relatorio = Relatorios.objects.last()
        self.assertTrue(relatorio.relator)

    def test_send_email(self):
        self.assertEqual(1, len(mail.outbox))
