from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messages(models.Model):
    text = models.TextField(max_length=75, verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    images = models.ImageField(
        'Картинка',
        upload_to='masseges/images/',
        blank=True,
        null=True,
    )
