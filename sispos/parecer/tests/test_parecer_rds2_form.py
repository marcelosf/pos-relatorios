from django.test import TestCase
from sispos.parecer.forms import Rds2Form


class FormRds2Test(TestCase):
    def setUp(self):
        self.form = Rds2Form()

    def test_has_fields(self):
        """It should has rde2 fields"""
        fields = ['desempenho', 'metodologia', 'resultados', 'esboco',
                  'atividades', 'status']
        for expected in fields:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))
