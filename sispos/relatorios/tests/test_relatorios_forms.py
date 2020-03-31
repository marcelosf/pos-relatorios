from django.test import TestCase
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

    def test_orientador_choices(self):
        """It should have a list of orientadores"""
        expected = [(self.orientador.pk, self.orientador.name)]
        self.assertListEqual(expected, self.form.fields['orientador'].choices)