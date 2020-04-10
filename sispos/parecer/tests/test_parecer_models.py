from django.test import TestCase
from sispos.parecer.models import Rds1


class ParecerModelsTest(TestCase):
    def setUp(self):
        self.obj = Rds1()

    def test_instance(self):
        """It should be an instance of Rds1"""
        self.assertIsInstance(self.obj, Rds1)

    def test_has_fields(self):
        """It should have fields"""
        fields = ['desempenho', 'revisao', 'definicao',
                  'plano', 'resultados', 'atividades']
        for expected in fields:
            with self.subTest():
                self.assertTrue(hasattr(self.obj, expected), msg='{} not found'.format(expected))
