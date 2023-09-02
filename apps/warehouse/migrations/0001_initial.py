# Generated by Django 4.0.6 on 2023-09-02 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('name', models.CharField(max_length=75, unique=True, verbose_name='Nome')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('name', models.CharField(max_length=75, unique=True, verbose_name='Nome')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
            ],
        ),
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('name', models.CharField(max_length=75, unique=True, verbose_name='Nome')),
                ('company', models.CharField(max_length=20, verbose_name='Empresa')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('name', models.CharField(max_length=75, unique=True, verbose_name='Nome')),
                ('min_amount', models.PositiveIntegerField(verbose_name='Estoque mínimo')),
                ('max_amount', models.PositiveIntegerField(verbose_name='Estoque máximo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.category', verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('amount', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('obs', models.TextField(blank=True, verbose_name='Observação')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_checkouts', to='warehouse.product', verbose_name='Produto')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester_checkouts', to='warehouse.requester', verbose_name='Solicitante')),
            ],
        ),
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('amount', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
                ('obs', models.TextField(blank=True, verbose_name='Observação')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_checkins', to='warehouse.product', verbose_name='Produto')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_checkins', to='warehouse.provider', verbose_name='Fornecedor')),
            ],
        ),
    ]