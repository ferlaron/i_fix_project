from django.db import models
from tinymce import HTMLField
# Create your models here.

class Post(models.Model):

    post_title = models.CharField('заголовок', max_length=254, blank=False, null=True, default=None)
    post_content = HTMLField('контент страницы', default='<span></span>')
    is_active = models.BooleanField("активен?", default=True)
    is_publicated = models.BooleanField("опубликован?", default=True)
    sort_order = models.PositiveIntegerField('порядок сортировки', null=True, blank=True, default=0)
    created = models.DateTimeField('добавлено',auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('обновлено',auto_now_add=False, auto_now=True)

    def __str__(self):
        strin = 'Пост: ' + self.post_title
        return strin

    class Meta:
        verbose_name = 'пост для главной страницы'
        verbose_name_plural = 'посты для главной страницы'
