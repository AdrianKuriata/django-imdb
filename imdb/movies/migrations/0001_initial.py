# Generated by Django 2.0.5 on 2018-05-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(max_length=550)),
                ('excerpt', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('duration_time', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
