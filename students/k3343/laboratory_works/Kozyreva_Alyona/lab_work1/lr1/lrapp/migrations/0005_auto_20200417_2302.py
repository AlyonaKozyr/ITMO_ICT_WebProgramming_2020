# Generated by Django 3.0.5 on 2020-04-17 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrapp', '0004_auto_20200417_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
