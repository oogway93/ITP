# Generated by Django 4.1.5 on 2023-02-27 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_author', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, message='Маленькое имя автора')], verbose_name='Имя автора поста')),
                ('last_name_author', models.CharField(blank=True, max_length=30, null=True, verbose_name='Фамилия автора поста')),
                ('topic_post', models.CharField(max_length=50, verbose_name='Тема поста')),
                ('short_info_post', models.TextField(max_length=400, verbose_name='Краткое описание поста')),
                ('photo_post', models.ImageField(upload_to='images/%m', verbose_name='Фото поста')),
                ('datetime_post', models.DateTimeField(auto_now=True, verbose_name='Дата и время создания поста')),
                ('url_post', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator(message='что-то не так с URL', schemes=['http', 'https', 'ftp', 'ftps'])], verbose_name='URL сайта для подробного описания')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['datetime_post'],
            },
        ),
    ]
