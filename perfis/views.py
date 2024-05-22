from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'usuario.html')