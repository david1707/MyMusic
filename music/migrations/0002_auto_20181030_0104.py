# Generated by Django 2.1.2 on 2018-10-30 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='bought_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='edition_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
