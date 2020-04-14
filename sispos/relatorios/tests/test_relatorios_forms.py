from django.test import TestCase
from django.forms import ModelChoiceField
from sispos.relatorios.forms import RelatoriosForm
from sispos.relatorios.tests import mock


class RelatoriosFormTest(TestCase):
    def setUp(self):
        mock_orientador = mock.MockUser()
        self.orientador = mock_orientador.make_orientador()
        self.form = RelatoriosForm()

    def test_instance(self):
        """Instance should be Relatorios"""
        self.assertIsInstance(self.form, RelatoriosForm)

    def test_has_fields(self):
        """Form should have fields"""
        fields = ['nome', 'orientador',
                  'programa', 'relatorio', 'encaminhamento']

        for expected in fields:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))

    def test_orientador_field_type(self):
        """orientador should be a modelChoiceField"""
        field = self.form.fields['orientador']
        self.assertIsInstance(field, ModelChoiceField)

    def test_orientador_is_required(self):
        """field orientador should be required"""
        field = self.form.fields['orientador']
        self.assertTrue(field.required)
    
    def test_has_semestre_field(self):
        """It must have the semestre field"""
        self.assertIn('semestre', list(self.form.fields))
