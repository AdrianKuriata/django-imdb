# Generated by Django 2.0.5 on 2018-05-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20180505_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(default=None, upload_to='media/covers'),
        ),
    ]
