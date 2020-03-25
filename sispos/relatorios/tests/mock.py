from sispos.accounts.models import User
from sispos.relatorios.models import Relatorios
from unittest import mock
from django.core.files import File


class MockUser():
    def make_user_data(self, **kwargs):
        user_default = {'login': '123456', 'name': 'Jetson Four',
                        'type': 'I'}
        user_data = dict(user_default, **kwargs)
        return user_data

    def save_user(self, data):
        user = User.objects.create_user(**data)
        return user


class MockRelatorio():
    def make_relatorio(self, **kwargs):
        relatorio_default = {'nome': 'Jetson', 'programa': 'Mestrado',
                             'orientador': 'Orientador 1',
                             'relatorio': self.make_file(),
                             'encaminhamento': self.make_file()}
        relatorio = dict(relatorio_default, **kwargs)
        return relatorio

    def save_relatorio(self, data):
        relatorios = Relatorios.objects.create(**data)
        return relatorios

    def make_file(self):
        file_mock = mock.MagicMock(spec=File, name='file-mock')
        file_mock.name = 'file.pdf'
        return file_mock
