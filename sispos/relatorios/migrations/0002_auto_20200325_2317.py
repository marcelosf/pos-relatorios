# Generated by Django 3.0.4 on 2020-03-25 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorios',
            name='encaminhamento',
            field=models.FileField(upload_to='encaminhamentos/%Y/%m/%d/', verbose_name='Encaminhamento'),
        ),
        migrations.AlterField(
            model_name='relatorios',
            name='relator',
            field=models.CharField(blank=True, max_length=128, verbose_name='Relator'),
        ),
        migrations.AlterField(
            model_name='relatorios',
            name='relatorio',
            field=models.FileField(upload_to='relatorios/%Y/%m/%d/', verbose_name='Relatório'),
        ),
    ]
