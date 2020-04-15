from django.test import TestCase
from sispos.parecer.models import Rds3
from sispos.parecer.tests import mock


class Rds3ModelTest(TestCase):
    def setUp(self):
        self.obj = Rds3()

    def test_fields_attr(self):
        """Rds3 must have attrs"""
        attrs = ['resultados', 'artigo', 'uuid', 'created_at']
        for expected in attrs:
            with self.subTest():
                self.assertTrue(hasattr(self.obj, expected))

    def test_has_foreign_keys(self):
        """Rds3 must have foreign keys"""
        fks = ['relatorio', 'relator']
        for expected in fks:
            with self.subTest():
                self.assertTrue(hasattr(Rds3, expected))

    def test_has_status_attr(self):
        """Rds3 must haeve status attribute"""
        self.assertTrue(hasattr(Rds3, 'status'))

    def test_persist_rds3(self):
        """It must persist rds3 data"""
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        mock_rds3 = mock.MockParecer()
        rds3_data = mock_rds3.make_rds3(relator=relator, relatorio=relatorio)
        Rds3.objects.create(**rds3_data)
        self.assertTrue(Rds3.objects.exists())
