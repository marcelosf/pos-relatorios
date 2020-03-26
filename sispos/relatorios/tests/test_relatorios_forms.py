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
        fields = ['nome', 'orientador',
                  'programa', 'relatorio', 'encaminhamento']

        for expected in fields:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))

    # def test_relator_choices(self):
    #     """Relator Choices should be > 1"""
    #     relator = self.form.fields['relator']
    #     self.assertTrue(len(relator.choices) > 0)

    # def test_relator_not_required(self):
    #     """relator field should not be required"""
    #     self.assertFalse(self.form.fields['relator'].required)
