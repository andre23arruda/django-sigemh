import os, uuid
from django.db import models
from django.utils.safestring import mark_safe
from core.models import Location
from equipments.methods.handle_image import generate_equipment_qrcode

from django.db.models.signals import post_save
from django.dispatch import receiver

PRIORITY = (
    (1, 'Baixo'),
    (2, 'Medio'),
    (3, 'Alto'),
    (4, 'Urgente'),
)

def create_id(length=5):
    uuid_str = str(uuid.uuid4())
    return uuid_str[:length]


def equipment_model_upload_to(instance, filename) -> str:
    '''Upload do arquivo para caminho especifico'''
    file_extension = filename.split('.')[-1]
    new_filename = f'{create_id()}.{file_extension}'
    return os.path.join('equipment_models', instance.id, new_filename)


class Manufacturer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    description = models.TextField(max_length=75, null=True, blank=True, verbose_name='Descrição')
    mean_failure_time = models.PositiveSmallIntegerField(default=2010, verbose_name='Tempo médio de falha (meses)')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.name


class EquipmentModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer_equipments', verbose_name='Fabricante')
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='type_equipments', verbose_name='Tipo de equipamento')
    operating_instructions = models.FileField(blank=True, upload_to='equipment_model_upload_to', verbose_name='Instruções de operação')
    image_1 = models.ImageField(blank=True, upload_to='equipment_model_upload_to', verbose_name='Foto 1')
    image_2 = models.ImageField(blank=True, upload_to='equipment_model_upload_to', verbose_name='Foto 2')
    image_3 = models.ImageField(blank=True, upload_to='equipment_model_upload_to', verbose_name='Foto 3')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.name


class Equipment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    equipment_model = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE, related_name='model_equipments', verbose_name='Modelo do equipamento')
    year_of_manufacture = models.PositiveSmallIntegerField(default=2010, verbose_name='Ano de fabricação')
    acquisition_date = models.DateField(blank=True, null=True, verbose_name='Data de aquisição')
    serial_number = models.CharField(max_length=75, unique=True, verbose_name='Número de série')
    patrimony = models.CharField(max_length=75, unique=True, verbose_name='Número de patrimônio')
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Localização')
    accident_history = models.BooleanField(default=True, verbose_name='Histórico de acidente')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')
    work_priority = models.PositiveSmallIntegerField(choices=PRIORITY, default=1, verbose_name='Prioridade')
    warranty_expiration = models.DateField(blank=True, null=True, verbose_name='Vencimento da garantia')
    external_maintenance = models.BooleanField(default=False, verbose_name='Manutenção externa')
    qr_code = models.ImageField(blank=True, upload_to='equipments/qr_code', verbose_name='QR Code')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return f'{self.equipment_model} - {self.patrimony}'

    def save_qr_code(self):
        qrcode_result = generate_equipment_qrcode(self)
        self.qr_code = qrcode_result
        print('xxx')
        self.save()

    def show_qr_code(self):
        return mark_safe(f'''
			<a href="{ self.qr_code.url }" target="_blank">
                See
			</a>'''
		)