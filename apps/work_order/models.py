from django.db import models
from django.contrib.auth.models import User
from equipments.models import Equipment

SERVICES = (
    (1, 'Manutenção corretiva'),
    (2, 'Manutenção preventiva'),
    (3, 'Calibração'),
)

STATUS = (
    (1, 'Aberto'),
    (2, 'Em atendimento'),
    (3, 'Finalizado'),
    (4, 'Impossível realizar'), # apenas gestor
)


class WorkOrder(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    checkin = models.DateTimeField(blank=True, null=True, verbose_name='Checkin')
    service = models.IntegerField(choices=SERVICES, default=1, verbose_name='Tipo de serviço')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='equipment_works', verbose_name='Equipamento')
    requester = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='requester_orders', verbose_name='Solicitante')
    request_description = models.TextField(blank=True, verbose_name='Descrição')
    job_description = models.TextField(blank=True, help_text='Útil para inspeção futura', verbose_name='Solução')
    status = models.IntegerField(choices=STATUS, default=1, verbose_name='Status')
    worker = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='worker_orders', verbose_name='Colaborador')
    checkout = models.DateTimeField(blank=True, null=True, verbose_name='Checkout')

    def __str__(self):
        return f'{ self.get_service_display() } - {self.created_at.strftime("%d/%m/%Y %H:%M:%S")}'