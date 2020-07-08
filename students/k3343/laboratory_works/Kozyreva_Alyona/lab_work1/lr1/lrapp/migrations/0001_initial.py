# Generated by Django 3.0.5 on 2020-04-16 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('group_number', models.CharField(max_length=50)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('subject', models.CharField(default='', max_length=50)),
                ('givingdate', models.DateField()),
                ('deadline', models.DateTimeField()),
                ('fines', models.CharField(max_length=500)),
                ('text', models.CharField(max_length=1000)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lrapp.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Q', 'Вопрос'), ('M', 'Замечена ошибка'), ('O', 'Другое')], max_length=50)),
                ('text', models.CharField(max_length=1000)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lrapp.Homework')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lrapp.Student')),
            ],
        ),
    ]