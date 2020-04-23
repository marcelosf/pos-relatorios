from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import mail
from django.conf import settings
from django.template.loader import render_to_string
from sispos.relatorios.models import Relatorios
from sispos.accounts.models import User


COORDENADOR_GROUP_NAME = 'orientadores'
RELATOR_GROUP_NAME = 'relatores'


@receiver(post_save, sender=Relatorios, dispatch_uid='send_coordenador_email')
def send_coordenador_email(sender, instance, **kwargs):
    if not instance.relator:
        email_group(COORDENADOR_GROUP_NAME, 'email_coordenador.txt')


@receiver(post_save, sender=Relatorios, dispatch_uid='send_orientador_email')
def send_relator_email(sender, instance, **kwargs):
    if instance.relator and (instance.state == 'waiting_relator'):
        email_group(RELATOR_GROUP_NAME, 'email_relator.txt')
        instance.state = 'relator_asigned'
        instance.save()


def email_group(group_name, template_name, **kwargs):
    users = User.objects.filter(groups__name=group_name)
    email_to = [user.main_email for user in users]
    body = render_to_string(template_name, kwargs)
    mail.send_mail(settings.EMAIL_SUBJECT, body, settings.EMAIL_FROM, email_to)
