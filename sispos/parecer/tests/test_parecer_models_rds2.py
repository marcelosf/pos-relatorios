from django.test import TestCase
from sispos.parecer.models import Rds2
from sispos.parecer.tests import mock


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

    def test_rds2_created(self):
        """Rds2 must be created"""
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        mock_rds2 = mock.MockParecer()
        rds2_data = mock_rds2.make_rds2(relator=relator, relatorio=relatorio)
        mock_rds2.save_rds2(rds2_data)

        self.assertTrue(Rds2.objects.exists())
