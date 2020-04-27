from django.test import TestCase
from sispos.relatorios.tests import mock
from sispos.relatorios.filters import RelatoriosFilter
from sispos.relatorios.models import Relatorios


class RelatoriosFilterGetTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        coordenador = mock_user.make_coordenador()
        self.client.force_login(coordenador)

    def test_filter_has_result(self):
        self.make_relatorio(nome='Jeger')
        query = '/relatorios/?nome=Jeger&orientador=&created='
        self.resp = self.send_request(query)
        self.assertContains(self.resp, 'Jeger')

    def test_filter_has_no_result(self):
        self.make_relatorio(nome='Jeger')
        query = '/relatorios/?nome=Mike&orientador=&created='
        self.resp = self.send_request(query)
        self.assertNotContains(self.resp, 'Jeger')

    def send_request(self, query):
        return self.client.get(query)

    def make_relatorio(self, **kwargs):
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio(**kwargs)
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        return relatorio


class RelatoriosFilterTest(TestCase):
    def setUp(self):
        self.make_relatorio(nome='Mozart')

    def test_filter_has_result(self):
        query = {'nome': 'Mozart'}
        queryset = Relatorios.objects.all()
        relatorios_filter = RelatoriosFilter(query, queryset)
        self.assertEqual(1, relatorios_filter.qs.count())

    def test_filter_has_no_result(self):
        relatorios_filter = self.set_filter(nome='Marc')
        self.assertEqual(0, relatorios_filter.qs.count())

    def set_filter(self, **query):
        queryset = Relatorios.objects.all()
        relatorios_filter = RelatoriosFilter(query, queryset)
        return relatorios_filter

    def make_relatorio(self, **kwargs):
        mock_relatorio = mock.MockRelatorio()
        relatorio_data = mock_relatorio.make_relatorio(**kwargs)
        relatorio = mock_relatorio.save_relatorio(relatorio_data)
        return relatorio
