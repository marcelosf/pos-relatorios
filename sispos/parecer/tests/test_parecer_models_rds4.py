from django.test import TestCase
from sispos.parecer.models import Rds4
from sispos.parecer.tests import mock


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

    def test_created(self):
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        mock_rds4 = mock.MockParecer()
        data = mock_rds4.make_rds4(relatorio=relatorio, relator=relator)
        Rds4.objects.create(**data)
        self.assertTrue(Rds4.objects.exists())
