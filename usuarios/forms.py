from django import forms 
from .models import Usuario, FotoPerfil

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nome', 'email', 'senha' ]
        
class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = FotoPerfil
        fields = ['id', 'imagem']