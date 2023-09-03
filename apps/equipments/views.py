from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Equipment
from .forms import OpenWorkForms, SelectWorkForms


@login_required(redirect_field_name='next', login_url='/admin/login/')
def equipment_detail(request: object, equipment_id: int):
    '''Selecionar ordem de serviço do equipamento'''
    equipment = get_object_or_404(Equipment, pk=equipment_id)

    if not request.user.profile.engineering_team:
        return redirect('equipments:equipment_open_work', equipment_id=equipment_id)

    context = {
        'page_title': 'Selecione a ordem de serviço do equipamento',
        'form': SelectWorkForms(instance=equipment),
        'equipment': equipment,
    }
    return render(request, 'equipments/equipment.html', context)


@login_required(redirect_field_name='next', login_url='/admin/login/')
def equipment_history(request: object, equipment_id: int):
    '''Histórico de ordens de serviço do equipamento'''
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    context = {
        'page_title': 'Histórico do equipamento',
        'works': equipment.equipment_works.all(),
        'equipment': equipment,
    }
    return render(request, 'equipments/equipment_history.html', context)


@login_required(redirect_field_name='next', login_url='/admin/login/')
def equipment_open_work(request: object, equipment_id: int):
    '''Abrir ordem de serviço para o equipamento'''
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    # has_works = equipment.equipment_works.filter(status=1, service=1).exists()
    has_works = False

    if request.method == 'POST':
        form = OpenWorkForms(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.equipment = equipment
            instance.requester = request.user
            instance.save()
            return JsonResponse({'message': 'ok'})

    context = {
        'page_title': 'Abrir ordem de serviço',
        'form': OpenWorkForms(),
        'equipment': equipment,
        'submit_disabled': has_works
    }

    if has_works:
        messages.warning(request, 'Equipamento já possui ordem de serviço em aberto')
    return render(request, 'equipments/equipment_open_work.html', context)
