from django.apps import AppConfig


class RelatoriosConfig(AppConfig):
    name = 'sispos.relatorios'

    def ready(self):
        import sispos.relatorios.signals
