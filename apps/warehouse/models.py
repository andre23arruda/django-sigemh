from django.db import models
from django.utils.translation import gettext_lazy as _


class Requester(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    company = models.CharField(max_length=20, verbose_name='Empresa')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.name


class Provider(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    uf = models.CharField(max_length=2, verbose_name='UF')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.name


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    min_amount = models.PositiveIntegerField(verbose_name='Estoque mínimo')
    max_amount = models.PositiveIntegerField(verbose_name='Estoque máximo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.name


class Checkin(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_checkins', verbose_name='Produto')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider_checkins', verbose_name='Fornecedor')
    amount = models.PositiveIntegerField(verbose_name='Quantidade')
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor')
    obs = models.TextField(blank=True, verbose_name='Observação')


class Checkout(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_checkouts', verbose_name='Produto')
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE, related_name='requester_checkouts', verbose_name='Solicitante')
    amount = models.PositiveIntegerField(verbose_name='Quantidade')
    obs = models.TextField(blank=True, verbose_name='Observação')
