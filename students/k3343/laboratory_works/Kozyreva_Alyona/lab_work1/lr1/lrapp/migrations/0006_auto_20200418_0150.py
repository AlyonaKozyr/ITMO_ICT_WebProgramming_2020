# Generated by Django 3.0.5 on 2020-04-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrapp', '0005_auto_20200417_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.CharField(choices=[('Вопрос', 'Вопрос'), ('Замечена ошибка', 'Замечена ошибка'), ('Другое', 'Другое')], max_length=50),
        ),
    ]