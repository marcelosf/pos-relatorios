from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.relatorios.tests import mock


class CoreViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render index.html template"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_base_template(self):
        """It should render base.html template"""
        self.assertTemplateUsed(self.resp, 'base.html')

    def test_menu_template(self):
        """It should render menu.html"""
        self.assertTemplateUsed(self.resp, 'menu.html')

    def test_bootstrap_scripts(self):
        scripts = ['bootstrap.min.css', 'bootstrap.min.js']

        for expected in scripts:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_menu_html(self):
        """Tamplte shoud render the menu html"""
        html = ['<nav', '>SISPOS</a>']

        for expected in html:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_template_html(self):
        """Template should render html items"""
        html = ['<a', 'Enviar Relatório']

        for expected in html:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_relatorios_card(self):
        """Template should render relatorios card"""
        card_content = ['Submissão de relatórios de atividade',
                        'Formulário para envio de relatórios de atividades de',
                        'Mestrado e Doutorado']

        for expected in card_content:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_enviar_relatorio_form_link(self):
        """Template should render relatorio form link"""
        self.assertContains(self.resp, r('relatorios:relatorios_new'))

    def test_login_button(self):
        """It should render the login button"""
        expected = 'Login'
        self.assertContains(self.resp, expected)

    def test_login_link(self):
        """It should render the login link"""
        expected = r('accounts:login')
        self.assertContains(self.resp, expected)

    def test_has_home_link(self):
        """Logo should be a link to home"""
        expected = 'href="/"'
        self.assertContains(self.resp, expected)

    def test_has_no_list_relatorios_link(self):
        """It should not render a link to relatorios list"""
        expected = 'href="{}"'.format(r('relatorios:relatorios_list'))
        self.assertNotContains(self.resp, expected)


class CoreViewOrientadorLoggedInTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        self.user = mock_user.make_orientador()
        self.client.force_login(self.user)
        self.resp = self.client.get(r('core:index'))

    def test_has_no_list_relatorios_link(self):
        """It should not render a link to relatorios list"""
        expected = 'href="{}"'.format(r('relatorios:relatorios_list'))
        self.assertNotContains(self.resp, expected)


class CoreViewTestUserLoggedIn(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        self.user = mock_user.make_coordenador()
        self.client.force_login(self.user)
        self.resp = self.client.get(r('core:index'))

    def test_logout_button(self):
        """It should render the logout button"""
        content = ['Logout', self.user.get_full_name()]
        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_has_no_login_button(self):
        """It should not render login button"""
        self.assertNotContains(self.resp, 'Login')

    def test_has_no_login_link(self):
        """It should not render login link"""
        self.assertNotContains(self.resp, r('accounts:login'))

    def test_has_list_relatorios_link(self):
        """It should render a link to relatorios list"""
        expected = 'href="{}"'.format(r('relatorios:relatorios_list'))
        self.assertContains(self.resp, expected)


class CoreViewsPageErrorTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/not-exists/')

    def test_response_status_code(self):
        """Status code should be 404"""
        self.assertEqual(404, self.resp.status_code)

    def test_template(self):
        """It should render 404.html"""
        self.assertTemplateUsed(self.resp, '404.html')

    def test_template_base(self):
        """It should render base.html template"""
        self.assertTemplateUsed(self.resp, 'base.html')
