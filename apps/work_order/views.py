from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import WorkOrder
from .forms import WorkForms


@login_required(redirect_field_name='next', login_url='/admin/login/')
def work(request: object, work_id: int):
    '''Exibe ordem de serviço com formulário'''
    instance = get_object_or_404(WorkOrder, pk=work_id)
    context = {
        'page_title': 'Ordem de serviço',
        'form': WorkForms(instance=instance),
        'work': instance,
    }
    return render(request, 'work_order/work.html', context)


@login_required(redirect_field_name='next', login_url='/admin/login/')
def work_start(request: object):
    '''Começa ordem de serviço'''
    if request.method == 'POST':
        work_id = request.POST.get('work_order')
        instance = get_object_or_404(WorkOrder, pk=work_id)
        instance.worker = request.user
        instance.status = 2
        if not instance.checkin:
            instance.checkin = timezone.now()
        instance.save()
    return redirect('work_order:work', work_id=work_id)


@login_required(redirect_field_name='next', login_url='/admin/login/')
def work_finish(request: object, work_id: int):
    '''Finaliza ordem de serviço'''
    instance = get_object_or_404(WorkOrder, pk=work_id)
    if request.method == 'POST':
        form = WorkForms(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = 3
            instance.checkout = timezone.now()
            instance.save()
            messages.success(request, 'Ordem de serviço finalizada com sucesso!')
    return redirect('equipments:equipment', equipment_id=instance.equipment.id)
