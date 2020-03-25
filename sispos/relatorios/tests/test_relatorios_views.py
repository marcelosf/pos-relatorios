from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.relatorios.tests import mock
from sispos.relatorios.models import Relatorios


class RelatoriosViewsGetTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        user_data = mock_user.make_user_data()
        user = mock_user.save_user(user_data)
        self.client.force_login(user)
        self.resp = self.client.get(r('relatorios:relatorios_new'))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render relatorios_novo.html"""
        self.assertTemplateUsed(self.resp, 'relatorios_novo.html')

    def test_base_template(self):
        """It should render base.html"""
        self.assertTemplateUsed(self.resp, 'base.html')

    def test_html_form(self):
        """Template should render html form"""
        html_form_itens = ((1, '<form'), (1, 'type="text"'), (3, '<select'),
                           (2, 'type="file"'), (1, 'type="submit"'))

        for count, expected in html_form_itens:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context_has_form(self):
        """Context shoud have form"""
        context = self.resp.context
        self.assertIn('form', context)

    def test_csrf_token(self):
        """Template should render csrf token"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_html_form_attrs(self):
        """form should set enctype and action attributes"""
        attrs = ['enctype="multipart/form-data"', 'action="/relatorios/novo"']
        for expected in attrs:
            with self.subTest():
                self.assertContains(self.resp, expected)


class RelatoriosViewsPostTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        mock_user = mock.MockUser()
        user_data = mock_user.make_user_data()
        user = mock_user.save_user(user_data)
        self.client.force_login(user)
        self.resp = self.client.post(r('relatorios:relatorios_new'),
                                     relatorio_data)

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_relatorio_created(self):
        """Relatorio count should be 1"""
        self.assertEqual(1, Relatorios.objects.count())


class RelatoriosViewLoggedOut(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('relatorios:relatorios_new'))

    def test_status_code(self):
        """Status code shoud be 302"""
        self.assertEqual(302, self.resp.status_code)
