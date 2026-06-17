from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Mahasiswa
from .forms import MahasiswaForm


def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)


@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()

    return render(request, 'mahasiswa/daftar.html', {
        'mahasiswas': mahasiswas
    })


@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data mahasiswa berhasil ditambahkan!')
            return redirect('daftar_mahasiswa')
    else:
        form = MahasiswaForm()
    return render(request, 'mahasiswa/form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, id):
    mahasiswa = get_object_or_404(Mahasiswa, id=id)
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data mahasiswa berhasil diperbarui!')
            return redirect('daftar_mahasiswa')
    else:
        form = MahasiswaForm(instance=mahasiswa)
    return render(request, 'mahasiswa/form.html', {'form': form, 'mahasiswa': mahasiswa})


@login_required(login_url='/accounts/login/')
def hapus_mahasiswa(request, id):
    mahasiswa = get_object_or_404(Mahasiswa, id=id)
    mahasiswa.delete()

    return redirect('daftar_mahasiswa')
