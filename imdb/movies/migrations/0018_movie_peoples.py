# Generated by Django 2.0.5 on 2018-05-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0001_initial'),
        ('movies', '0017_auto_20180509_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='peoples',
            field=models.ManyToManyField(related_name='movies', through='peoples.MoviePeople', to='peoples.People'),
        ),
    ]
