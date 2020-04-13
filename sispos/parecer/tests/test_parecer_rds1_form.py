from django.test import TestCase
from sispos.parecer.forms import Rds1Form


class ParecerRds1FormTest(TestCase):
    def setUp(self):
        self.form = Rds1Form()

    def test_has_fields(self):
        """Form shoud have the required fields"""
        fields = ['desempenho', 'revisao', 'definicao', 'plano',
                  'resultados', 'atividades']
        for expected in fields:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))

    def test_has_status_field(self):
        """It should have status field"""
        self.assertIn('status', list(self.form.fields))
