from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'main/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'main/signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')