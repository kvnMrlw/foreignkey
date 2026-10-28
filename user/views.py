from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as log
from django.contrib.auth.decorators import login_required
from .models import Produto
from django.contrib.auth import logout

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render (request, 'cadastro.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).exists()
        if user:
            return HttpResponse("esse nome de usuario já existe")

        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
        

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            log(request, user)
            return redirect('plataforma')
        else:
            return HttpResponse("Nome ou senha incorreto")


@login_required
def plataforma(request):
    if request.method == "GET":
        produto = Produto.objects.filter(criado_por = request.user )
        return render(request, 'plataforma.html', {'produto' : produto})
    elif request.method == "POST":
        Produto.objects.create(
            produto=request.POST.get('produto'),
            preco=request.POST.get('preco'),
            criado_por=request.user,
    )
    return redirect('plataforma')

       


def logout_view(request):
    logout(request)
    return redirect('login')


        
