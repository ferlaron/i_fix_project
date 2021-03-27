from django.db import models
import cyrtranslit
from django.utils.text import slugify


class Option(models.Model):

    option_name = models.CharField('имя опции', max_length=254, blank=False, null=True, default=None, unique=True)
    option_value = models.CharField('значение опции', max_length=254, blank=False, null=True, default=None)
    slug = models.CharField(max_length=255, blank=True, default = None)
    created = models.DateTimeField('добавлено',auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('обновлено',auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.option_name

    def save(self, *args, **kwargs):

        cyr = cyrtranslit.to_latin(self.option_name, 'ru')
        stri = slugify(cyr)
        self.slug = stri

        super(Option, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'опция проекта'
        verbose_name_plural = 'опции проекта'
