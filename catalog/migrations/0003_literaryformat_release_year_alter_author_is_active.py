# Generated by Django 4.1.1 on 2022-09-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_author_pseudonym"),
    ]

    operations = [
        migrations.AddField(
            model_name="literaryformat",
            name="release_year",
            field=models.IntegerField(default=2015),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="author",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]
