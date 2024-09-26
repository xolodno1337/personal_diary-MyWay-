from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Diary(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(upload_to='diary/image', verbose_name='Превью события', **NULLABLE)
    context = models.TextField(verbose_name='Описание события')
    date_event = models.CharField(max_length=20, verbose_name='Дата события', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи', **NULLABLE)
    is_active = models.BooleanField(default=True, help_text='Разрешить эту запись видеть всем?')
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись дневника'
        verbose_name_plural = 'Записи дневника'
