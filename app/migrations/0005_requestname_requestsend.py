# Generated by Django 2.0 on 2021-10-24 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_employee_hr'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Requestsend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(auto_now_add=True)),
                ('enddate', models.DateField(auto_now_add=True)),
                ('des', models.CharField(default='Description', max_length=100)),
                ('status', models.CharField(default='False', max_length=200)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Admin')),
                ('reqna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.RequestName')),
            ],
        ),
    ]