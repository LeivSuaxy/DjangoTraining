from django.shortcuts import render, redirect

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

class VRegistro(View):

    def get(self, request):
        print('Entrando en funcion get')
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            print('Is valid')
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        else:
            print('Is invalid')

            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, 'registro/registro.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Incorrect username or password')
                return render(request, 'login')
        else:
            messages.error(request, 'Incorrect Info')
    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})
