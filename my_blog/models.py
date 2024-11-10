from django.db import models


class My_blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(max_length=500, verbose_name='содержимое')
    preview = models.ImageField(upload_to='media/images/', verbose_name='изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    publication_sign = models.BooleanField
    number_of_views = models.Count