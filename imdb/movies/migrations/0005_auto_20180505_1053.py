# Generated by Django 2.0.5 on 2018-05-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20180505_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(default=None, upload_to='static/images/covers'),
        ),
    ]
