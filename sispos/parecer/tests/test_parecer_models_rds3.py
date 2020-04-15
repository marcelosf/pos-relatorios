from django.test import TestCase
from sispos.parecer.models import Rds3


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