from django.test import TestCase
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey
from sispos.relatorios.models import Relatorios
from sispos.relatorios.tests import mock
from django.shortcuts import resolve_url as r


class RelatoriosTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        self.obj = Relatorios.objects.create(**relatorio_data)

    def test_relatorio_instance(self):
        """Obj should be an instance of Relatorio"""
        self.assertIsInstance(self.obj, Relatorios)

    def test_relatorio_create(self):
        """Relatorios count should be 1"""
        self.assertEqual(1, Relatorios.objects.count())

    def test_relator_not_required(self):
        """relator field should be nullable"""
        field = Relatorios.relator.field
        self.assertTrue(field.null)

    def test_relator_is_foreign_key(self):
        """relator field should be a foreignkey"""
        field = Relatorios.relator.field
        self.assertIsInstance(field, ForeignKey)

    def test_relatorio_is_file_field(self):
        """relatorio should be FileField"""
        field = Relatorios.relatorio.field
        self.assertIsInstance(field, FileField)

    def test_encaminhamento_is_file_field(self):
        """encaminhamento should be FileField"""
        field = Relatorios.encaminhamento.field
        self.assertIsInstance(field, FileField)

    def test_has_user(self):
        """It should have user_id property"""
        self.assertTrue(hasattr(self.obj, 'user'))

    def test_relatorios_has_created_field(self):
        """Relatorio should have a created field"""
        self.assertTrue(hasattr(self.obj, 'created'))

    def test_relatorios_has_uuid_field(self):
        """Relatorio should have a created field"""
        self.assertTrue(hasattr(self.obj, 'uuid'))

    def test_get_absolute_url(self):
        """It should be /relatorios/update"""
        expected = r('relatorios:relatorios_update', slug=str(self.obj.uuid))
        self.assertEqual(expected, self.obj.get_absolute_url())

    def test_has_semestre_attr(self):
        """It must have semestre attr"""
        self.assertTrue(hasattr(self.obj, 'semestre'))
