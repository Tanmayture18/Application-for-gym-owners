# Generated by Django 3.2.6 on 2021-09-28 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='date',
        ),
    ]
