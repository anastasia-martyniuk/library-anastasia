# Generated by Django 4.1.1 on 2022-09-29 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_literaryformat_annotation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='literaryformat',
            name='annotation',
        ),
        migrations.RemoveField(
            model_name='literaryformat',
            name='release_year',
        ),
    ]
