# Generated by Django 2.2.19 on 2021-03-20 13:50

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(default='default_title', max_length=254, null=True, verbose_name='заголовок')),
                ('post_content', tinymce.models.HTMLField(default='<span></span>', verbose_name='контент страницы')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен?')),
                ('publicated', models.BooleanField(default=True, verbose_name='опубликован?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='добавлено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
            ],
            options={
                'verbose_name': 'пост для главной страницы',
                'verbose_name_plural': 'посты для главной страницы',
            },
        ),
    ]
