from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.db.models.query import QuerySet
from django_filters import FilterSet
from sispos.relatorios.tests import mock


class ViewsRelatoriosListTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        self.relatorio = mock_relatorio.save_relatorio(relatorio_data)
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        self.client.force_login(relator)
        self.resp = self.client.get(r('relatorios:relatorios_list'))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It shoul render relatorios_list.html"""
        self.assertTemplateUsed(self.resp, 'relatorios_list.html')

    def test_template_base(self):
        """It should render base.html"""
        self.assertTemplateUsed(self.resp, 'base.html')

    def test_context(self):
        """relatorios_list should be in context"""
        context = self.resp.context
        self.assertIn('relatorios_list', context)

    def test_relatorios_list(self):
        """relatorios list shoul wbe a QuerySet"""
        relatorios_list = self.resp.context['relatorios_list']
        self.assertIsInstance(relatorios_list, QuerySet)

    def test_title(self):
        """Template should render title"""
        expected = 'Lista de relatórios'
        self.assertContains(self.resp, expected)

    def test_html_tags(self):
        """Template should render html table tags"""
        tags = ['<table', '<th', '<tr']

        for expected in tags:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_table_collumns(self):
        """Table should contains collums name"""
        collumns = ['Nome', 'Envio', 'Orientador']

        for expected in collumns:
            self.assertContains(self.resp, expected)

    def test_has_detalhar_button(self):
        """Template should render detalhar button"""
        expected = '<a class="btn btn-sm btn-outline-primary"'
        self.assertContains(self.resp, expected)

    def test_has_filter(self):
        """Template should render filters"""
        filter = self.resp.context['filter']
        self.assertIsInstance(filter, FilterSet)

    def test_filter_fields(self):
        """Template should render filter Fields"""
        fields = ['name="nome"', 'name="orientador"', 'name="created"']

        for expected in fields:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_detalhar_link(self):
        """Template should render the detalhar button link"""
        relatorio_uuid = str(self.relatorio.uuid)
        url = '/relatorios/update/{}/'.format(relatorio_uuid)
        expected = 'href="{}"'.format(url)
        self.assertContains(self.resp, expected)

    def test_relator(self):
        """List shoud have relator column"""
        self.assertContains(self.resp, 'Relator')

    def test_has_sidebar_menu(self):
        """It should render the sidebar menu template"""
        self.assertTemplateUsed(self.resp, 'sidebar.html')


class ViewsRelatoriosListLoggedOutTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('relatorios:relatorios_list'))

    def test_page_redirect(self):
        """Status code should be 302"""
        self.assertEqual(302, self.resp.status_code)
