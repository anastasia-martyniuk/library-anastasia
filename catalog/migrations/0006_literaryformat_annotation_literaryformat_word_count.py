# Generated by Django 4.1.1 on 2022-09-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_remove_literaryformat_annotation_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="literaryformat",
            name="annotation",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="literaryformat",
            name="word_count",
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
