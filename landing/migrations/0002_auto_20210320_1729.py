# Generated by Django 2.2.19 on 2021-03-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=None, max_length=254, null=True, verbose_name='заголовок'),
        ),
    ]
