from apps.archivo.views import archivo, download_file, proquest_zip
from django.urls import path
from apps.archivo import views

app_name = 'archivo'
urlpatterns = [
    path('', archivo, name = 'index'),
    path('nuevo/', views.Archivo_form.as_view(), name='nuevo'),
    path('media/<str:path_f>/<str:file_name>', download_file, name='descargar'),
    path('single/', views.Proquest_form.as_view(), name='single'),
    path('zip/<int:pk>', proquest_zip, name='zip'),
    path('edit/<int:pk>', views.Proquest_update.as_view(), name='edit')
]