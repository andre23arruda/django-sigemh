from django.urls import path
from .views import equipment, equipment_history, equipment_open_work

app_name = 'equipments'

urlpatterns = [
    path('equipments/<int:equipment_id>/', equipment, name='equipment'),
    path('equipments/<int:equipment_id>/history', equipment_history, name='equipment_history'),
    path('equipments/<int:equipment_id>/open_work', equipment_open_work, name='equipment_open_work'),
#     path('register_participant', participant_form, name='register_participant'),
#     path('register_success', success_participant_form, name='register_success'),
#     path('register_error', error_participant_form, name='register_error'),
#     path('see_qrcode/<str:participant_id>', see_qrcode, name='see_qrcode'),
#     path('see_pdf/<str:event_id>/<str:participant_id>', see_pdf, name='see_pdf'),
]
