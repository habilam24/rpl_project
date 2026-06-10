from django.shortcuts import render

def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Belajar Django Templates dan Static Files'
    }

    return render(request, 'mahasiswa/index.html', context)
from django.shortcuts import render
from .models import Mahasiswa

from django.contrib.auth.decorators import login_required
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()

    return render(
        request,
        'mahasiswa/daftar.html',
        {'mahasiswas': mahasiswas}
    )