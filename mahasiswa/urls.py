from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path(
        'daftar/',
        views.daftar_mahasiswa,
        name='daftar_mahasiswa',
    ),
    path('', RedirectView.as_view(url='daftar/')),
]