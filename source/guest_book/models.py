from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class GuestBook(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(null=False, verbose_name='Email')
    text = models.TextField(max_length=2000, null=False, blank=True, verbose_name='Текст')
    create_date = models.DateTimeField(null=False, auto_now=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(null=False, auto_now=True, verbose_name='Дата редактировнаия')
    status = models.CharField(null=False, choices=STATUS_CHOICES, max_length=7, default='active', verbose_name='Cтатус')

def __str__(self):
    return f'{self.name} {self.email} {self.text} {self.status}'


class Meta:
    db_table = 'GuestBook'
    verbose_name = 'Гостевая книга'
    verbose_name_plural = 'Гостевые книги'