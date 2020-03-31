from sispos.accounts.models import User
from sispos.relatorios.models import Relatorios
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

    def make_coordenador(self):
        user_data = self.make_user_data(login='334455')
        coordendor = self.save_user(user_data)
        self.set_permission('change_relatorios', coordendor)
        return coordendor

    def make_orientador(self):
        user_data = self.make_user_data(name='Orientador 1')
        orientador = self.save_user(user_data)
        self.set_group(group_name='orientadores', user=orientador)
        return orientador

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
