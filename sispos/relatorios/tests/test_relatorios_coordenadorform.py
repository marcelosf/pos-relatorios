from django.test import TestCase
from sispos.relatorios.forms import CoordenadorForm


class CoordenadorFormTest(TestCase):
    def setUp(self):
        self.form = CoordenadorForm()

    def test_form_has_fields(self):
        fields = list(self.form.fields.keys())
        self.assertIn('relator', fields)
