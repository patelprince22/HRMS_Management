# Generated by Django 2.0 on 2021-10-10 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210913_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='t_c',
        ),
    ]
