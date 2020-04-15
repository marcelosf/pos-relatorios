from django.test import TestCase
from sispos.parecer.forms import Rds3Form


class Rds3FormTest(TestCase):
    def setUp(self):
        self.form = Rds3Form()

    def test_form_fields(self):
        """It must contain the form fields"""
        fields = ['resultados', 'artigo', 'atividades']
        for expected in fields:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))

    def test_has_status_attr(self):
        """It must have status attr"""
        self.assertIn('status', list(self.form.fields))
