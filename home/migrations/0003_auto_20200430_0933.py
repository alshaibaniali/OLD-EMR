# Generated by Django 3.0.3 on 2020-04-30 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200412_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='last_login',
        ),
    ]
