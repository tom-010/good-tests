# Generated by Django 2.2.8 on 2021-02-17 06:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('desiderata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiderata',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
