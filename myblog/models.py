from django.core import validators
from django.db import models



class Post(models.Model):
    first_name_author = models.CharField('Имя автора поста', max_length=15,
                                         validators=[validators.MinLengthValidator(3, message='Маленькое имя автора')])
    last_name_author = models.CharField('Фамилия автора поста', max_length=30, blank=True, null=True)
    topic_post = models.CharField('Тема поста', max_length=50)
    short_info_post = models.TextField('Краткое описание поста', max_length=400)
    photo_post = models.ImageField('Фото поста', upload_to='images/%m')
    datetime_post = models.DateTimeField('Дата и время создания поста', auto_now=True)
    url_post = models.URLField('URL сайта для подробного описания', blank=True, null=True, validators=[
        validators.URLValidator(schemes=['http', 'https', 'ftp', 'ftps'], message='что-то не так с URL')])

    def __str__(self):
        return f'{self.first_name_author}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['datetime_post']


