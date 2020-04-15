from django.test import TestCase
from sispos.parecer.models import Rds4

class Rds4ModelTest(TestCase):
    def setUp(self):
        self.obj = Rds4()

    def test_fields(self):
        """Rds4 must have fields"""
        fields = ['perspectiva', 'status', 'relator',
                  'relatorio', 'created_at', 'uuid']
        for expected in fields:
            with self.subTest():
                msg = '{} not found'.format(expected)
                self.assertTrue(hasattr(Rds4, expected), msg=msg)
