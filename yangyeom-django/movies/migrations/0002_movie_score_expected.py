# Generated by Django 2.2.7 on 2019-11-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='score_expected',
            field=models.IntegerField(default=0),
        ),
    ]
