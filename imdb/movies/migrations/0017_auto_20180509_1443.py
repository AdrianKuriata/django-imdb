# Generated by Django 2.0.5 on 2018-05-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_auto_20180509_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(max_length=120, unique=True),
        ),
    ]