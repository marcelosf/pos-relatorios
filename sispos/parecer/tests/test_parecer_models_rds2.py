from django.test import TestCase
from sispos.parecer.models import Rds2


class ParecerRds2ModelsTest(TestCase):
    def setUp(self):
        self.obj = Rds2()

    def test_rds2_attr(self):
        """It must contain Rds2 fields"""
        fields = ['desempenho', 'metodologia', 'resultados', 'uuid',
                  'esboco', 'atividades', 'status', 'created_at']

        for expected in fields:
            with self.subTest():
                msg = '{} not found'.format(expected)
                self.assertTrue(hasattr(self.obj, expected), msg=msg)
