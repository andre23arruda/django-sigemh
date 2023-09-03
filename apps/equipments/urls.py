from django.urls import path
from .views import (
    equipment_detail,
    equipment_history,
    equipment_open_work,
)

app_name = 'equipments'

urlpatterns = [
    path('equipments/<int:equipment_id>/', equipment_detail, name='equipment'),
    path('equipments/<int:equipment_id>/history', equipment_history, name='equipment_history'),
    path('equipments/<int:equipment_id>/open_work', equipment_open_work, name='equipment_open_work'),
]
