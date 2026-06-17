from django import forms
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['nim', 'nama', 'programstudi', 'angkatan']
        widgets = {
            'nim': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan NIM'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama Lengkap'}),
            'programstudi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Program Studi'}),
            'angkatan': forms.NumberInput(attrs={'class': 'form-control'}),
        }