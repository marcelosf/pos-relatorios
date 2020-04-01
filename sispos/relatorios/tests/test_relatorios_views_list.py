from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.db.models.query import QuerySet


class ViewsRelatoriosListTest(TestCase):
    def setUp(self):
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
