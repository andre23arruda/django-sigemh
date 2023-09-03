from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(redirect_field_name='next', login_url='/admin/login/')
def request_success(request):
    '''Sucesso na requisição'''
    context = {'page_title': 'Sucesso'}
    return render(request, 'success.html', context)


@login_required(redirect_field_name='next', login_url='/admin/login/')
def request_error(request):
    '''Erro na requisição'''
    context = {'page_title': 'Erro'}
    return render(request, 'error.html', context)