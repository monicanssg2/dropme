# Generated by Django 4.1.7 on 2023-02-26 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_api', '0002_alter_machine_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='qr_code',
            field=models.CharField(help_text='Format: required, max-length:50', max_length=50, verbose_name='Machine Code'),
        ),
    ]
