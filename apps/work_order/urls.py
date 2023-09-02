from django.urls import path
from .views import work, work_start, work_finish

app_name = 'work_order'

urlpatterns = [
    path('work/<int:work_id>/', work, name='work'),
    path('work/start', work_start, name='work_start'),
    path('work/<int:work_id>/finish', work_finish, name='work_finish'),
]
