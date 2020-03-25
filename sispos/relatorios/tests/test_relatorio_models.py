from django.test import TestCase
from sispos.relatorios.models import Relatorios


class RelatoriosTest(TestCase):
    def setUp(self):
        relatorio = dict(nome='Jadelson', relator='Relatonildo',
                         orientador='Sidney', programa='Mestrado',
                         relatorio='relatorio.pdf',
                         encaminhamento='enc.pdf')
        self.obj = Relatorios.objects.create(**relatorio)

    def test_relatorio_instance(self):
        """Obj should be an instance of Relatorio"""
        self.assertIsInstance(self.obj, Relatorios)

    def test_relatorio_create(self):
        """Relatorios count should be 1"""
        self.assertEqual(1, Relatorios.objects.count())

    def test_relator_not_required(self):
        """relator field should not be required"""
        field = Relatorios.relator.field
        self.assertTrue(field.blank)
