# Generated by Django 2.2.7 on 2019-11-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20191127_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='score_avg',
            field=models.FloatField(default=0),
        ),
    ]
