from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.core import mail
from django.conf import settings
from django.template.loader import render_to_string
from sispos.relatorios.models import Relatorios


@receiver(post_save, sender=Relatorios, dispatch_uid='send_coordenador_email')
def send_coordenador_email(sender, instance, **kwargs):
    if not instance.relator:
        change_relatorio = Permission.objects.get(codename='change_relatorios')
        coordenadores = change_relatorio.user_set.all()
        email_to = [user.main_email for user in coordenadores]

        mail.send_mail(settings.EMAIL_SUBJECT, body(),
                       settings.EMAIL_FROM, email_to)


def body():
    return render_to_string('email_coordenador.txt', {})
