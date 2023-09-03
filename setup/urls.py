from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import request_error, request_success


admin.site.index_title = 'Área de Administração'
admin.site.site_title = 'Estoque de medicamentos'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('equipments.urls')),
    path('', include('work_order.urls')),
    path('success', request_success, name='request_success'),
    path('error', request_error, name='request_error'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)