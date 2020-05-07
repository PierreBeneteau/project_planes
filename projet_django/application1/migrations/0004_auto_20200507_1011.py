# Generated by Django 2.2.5 on 2020-05-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0003_auto_20200505_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airports_arr',
            name='lat',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='airports_arr',
            name='lon',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='lat',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='lon',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]