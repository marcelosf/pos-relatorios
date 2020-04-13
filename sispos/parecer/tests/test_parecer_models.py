from django.test import TestCase
from sispos.parecer.models import Rds1
from sispos.parecer.tests import mock


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
                self.assertTrue(hasattr(self.obj, expected),
                                msg='{} not found'.format(expected))

    def test_created(self):
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)

        data = {'desempenho': 'desempenho', 'revisao': 'revisao',
                'definicao': 'definicao', 'plano': 'plano',
                'resultados': 'resultados', 'atividades': 'atividades',
                'relator': relator, 'relatorio': relatorio}
        Rds1.objects.create(**data)

        self.assertTrue(Rds1.objects.exists())

    def test_has_uuid_attr(self):
        """Rds1 should contain the uuid attr"""
        obj = self.make_parecer()
        self.assertTrue(hasattr(obj, 'uuid'))

    def test_get_absolute_url(self):
        """It dhould get the absolute url"""
        obj = self.make_parecer()
        expected = '/parecer/rds1/{}'.format(str(obj.uuid))
        self.assertEqual(expected, obj.get_absolute_url())

    def make_parecer(self):
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(relatorio_data)

        data = {'desempenho': 'desempenho', 'revisao': 'revisao',
                'definicao': 'definicao', 'plano': 'plano',
                'resultados': 'resultados', 'atividades': 'atividades',
                'relator': relator, 'relatorio': relatorio}
        return Rds1.objects.create(**data)
