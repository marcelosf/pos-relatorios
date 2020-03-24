from django.test import TestCase
from sispos.relatorios.forms import Relatorios


class RelatoriosFormTest(TestCase):
    def setUp(self):
        self.form = Relatorios()

    def test_instance(self):
        """Instance should be Relatorios"""
        self.assertIsInstance(self.form, Relatorios)

    def test_has_fields(self):
        """Form should have fields"""
        fields = ['nome', 'relator', 'orientador',
                  'programa', 'relatorio', 'encaminhamento']

        for expected in fields:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))
