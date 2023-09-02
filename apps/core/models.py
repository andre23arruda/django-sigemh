from django.db import models


class TechnicalStandard(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    title = models.CharField(max_length=200, unique=True, verbose_name='Título')
    year = models.PositiveIntegerField(default=2010, verbose_name='Ano')
    file = models.FileField(upload_to='technical_standards/%Y/%M/%D', verbose_name='Arquivo')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.title

class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.name
