from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    nick_name = models.CharField(max_length=50, verbose_name='Ник на сайте', help_text='Укажите ваше ник на сайте',
                                 **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Укажите ваш Email')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', help_text='Загрузите ваш аватар',
                               **NULLABLE)
    birthday = models.DateField(verbose_name='Дата рождения', help_text='Укажите дату вашего рождения', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', help_text='Укажите ваш номер телефона',
                             **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='Token', **NULLABLE)
    tg_nick = models.CharField(max_length=50, verbose_name='Ник телеграмм', help_text='Укажите ваше имя в телеграмме',
                               **NULLABLE)
    vk_nick = models.CharField(max_length=50, verbose_name='Страница в ВКонтакте',
                               help_text='Укажите вашу страницу в ВКонтакте', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
