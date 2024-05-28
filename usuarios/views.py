from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import FotoPerfil, Usuario
from .forms import FotoPerfilForm
from django.db import IntegrityError

from django.shortcuts import HttpResponse
from django.conf import settings
import os

def home(request):
    infos = {}
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')    
        usuario = Usuario.objects.get(id_usuario=user_id)
        infos['usuario'] = usuario
        
    infos['foto_perfil'] = FotoPerfil.objects.get(id=1)
    return render(request,'logado.html', infos)

def cadastro(request):
    infos = {}
    if 'error_msg' in request.session:
        infos['error_msg'] = request.session.get('error_msg')
    
    return render(request,'index.html', infos)

# def cadastrando(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         if Usuario.objects.filter(email=email).first() is not None:
#             request.session['error_msg'] = 'E-mail ja registrado'
#             return redirect(reverse('cadastro'))
#         else:
#             novo_usuario = Usuario()
#             novo_usuario.nome = request.POST.get('nome')
#             novo_usuario.email = request.POST.get('email')
#             novo_usuario.senha = make_password(request.POST.get('senha'))
#             novo_usuario.save()
            
#             email = request.POST.get('email')
#             user = Usuario.objects.filter(email=email).first()

#             request.session['user_id'] = user.id_usuario

#             print(novo_usuario.nome)
#             return redirect(reverse('cadastro.html'))
#     else:
#         return render(request, 'index.html')
    

def cadastrando(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        # Debugging print statements
        print(f"Received data: email={email}, nome={nome}, senha={senha}")

        if not email or not nome or not senha:
            request.session['error_msg'] = 'Todos os campos devem ser preenchidos.'
            return redirect(reverse('cadastro'))

        if Usuario.objects.filter(email=email).exists():
            request.session['error_msg'] = 'E-mail já existe'
            return redirect(reverse('cadastro'))
        
        else:
            try:
                novo_usuario = Usuario(
                    nome=nome,
                    email=email,
                    senha=make_password(senha)
                )
                novo_usuario.save()
                request.session['user_id'] = novo_usuario.pk
                return redirect(reverse('home'))
            except Exception as e:
                request.session['error_msg'] = f'Error saving user: {e}'
                return redirect(reverse('cadastro'))
    else:
        return redirect(reverse('cadastro'))


def lista_usuarios(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    usuarios['imagens'] = FotoPerfil.objects.all()
    return render(request, 'usuarios.html',usuarios)

def login(request):
    infos = {}
    if 'error_msg' in request.session:
        infos['error_msg'] = request.session.get('error_msg')
    if 'email' in request.session:
        infos['email'] = request.session.get('email')
    
    return render(request,'login.html', infos)

def logando(request):
    email = request.POST.get('email')
    user = Usuario.objects.filter(email=email).first()
    if user is None:
        request.session['error_msg'] = 'Email Incorreto'
        request.session['email'] = email
        
        return redirect(reverse('login'))
    
    request_senha = request.POST.get('senha')
    user_senha = user.senha 

    if check_password(request_senha, user_senha):
        request.session['user_id'] = user.id_usuario
        
        return redirect(reverse('home'))    
    else:
        request.session['error_msg'] = 'Senha Incorreta!'
        request.session['email'] = email
        
        return redirect(reverse('login'))

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        
    origem = request.GET.get('origem')
    if origem:
        return redirect(origem)
    else:
        return redirect(reverse('home'))
    
def del_vars(request):
    cache = {'email', 'error_msg'}
    for var in cache:
        if var in request.session:
            del request.session[var]
    return HttpResponse(status=200)

def upload(request):
    infos = {}
    if 'error_msg' in request.session:
        infos['error_msg'] = request.session['error_msg']
    return render(request, 'upload.html', infos)

def uploading(request):
    if request.method == 'POST':
        formulario = FotoPerfilForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = FotoPerfilForm()
    return render(request, 'upload.html', {'formulario': formulario})
    
    
    '''
    imagem = request.POST.get('imagem')
    nova_imagem = FotoPerfil()
    nova_imagem.imagem = imagem
    nova_imagem.save()
    request.session['error_msg'] = 'Foto registrada com sucesso'
    
    return redirect(reverse('upload'))
    '''

def verificar_imagem(request):
    certo = FotoPerfil.objects.get(id=8)
    certo.delete()
    return redirect(reverse('home'))