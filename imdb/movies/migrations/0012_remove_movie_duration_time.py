# Generated by Django 2.0.5 on 2018-05-06 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20180506_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='duration_time',
        ),
    ]
