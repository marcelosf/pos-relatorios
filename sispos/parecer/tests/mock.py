from sispos.accounts.models import User
from sispos.relatorios.models import Relatorios
from sispos.parecer.models import Rds1, Rds2
from unittest import mock
from django.core.files import File
from django.contrib.auth.models import Permission, Group


class MockUser():
    def make_user_data(self, **kwargs):
        user_default = {'login': '123456', 'name': 'Jetson Four',
                        'type': 'I', 'main_email': 'jetsonfour@mailinator.com'}
        user_data = dict(user_default, **kwargs)
        return user_data

    def save_user(self, data):
        user = User.objects.create_user(**data)
        return user

    def make_relator(self):
        user_data = self.make_user_data(name='relator')
        relator = self.save_user(user_data)
        self.set_group(group_name='relatores', user=relator)
        return relator

    def set_permission(self, perm_codename, user):
        perms = Permission.objects.get(codename=perm_codename)
        user.user_permissions.set([perms])

    def set_group(self, group_name, user):
        group, created = Group.objects.get_or_create(**{'name': group_name})
        user.groups.set([group])


class MockRelatorio():
    def make_relatorio(self, **kwargs):
        relatorio_default = {'nome': 'Jetson Four', 'programa': 'Mestrado',
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


class MockParecer():
    def make_parecer(self, **kwargs):
        parecer_default = {'desempenho': 'desempenho', 'revisao': 'revisao',
                           'definicao': 'definicao', 'plano': 'plano',
                           'resultados': 'resultados',
                           'atividades': 'atividades', 'status': 'aprovado'}
        return dict(parecer_default, **kwargs)

    def save_parecer(self, parecer):
        return Rds1.objects.create(**parecer)

    def make_rds2(self, **kwargs):
        rds2_default = {'desempenho': 'desempenho',
                        'metodologia': 'metodologia',
                        'resultados': 'resultados', 'esboco': 'esboco',
                        'atividades': 'atividades', 'status': 'aprovado'}
        return dict(rds2_default, **kwargs)

    def save_rds2(self, parecer):
        return Rds2.objects.create(**parecer)

    def make_rds3(self, **kwargs):
        rds3_default = {'resultados': 'resultados', 'artigo': 'artigo',
                        'atividades': 'atividades', 'status': 'aprovado'}
        return dict(rds3_default, **kwargs)
