# Generated by Django 4.1.1 on 2022-09-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_literaryformat_release_year_alter_author_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='literaryformat',
            name='annotation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
