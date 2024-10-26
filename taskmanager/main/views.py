from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm
from .models import Post


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/') # Перенаправляем на список постов
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = PostForm(instance=post)
        return render(request, 'main/edit_post.html', {'form': form})
    else:
        return redirect('/')

@login_required
def delete_post(request, post_id):
    if request.method == 'POST':
        try:
            post = post = get_object_or_404(Post, pk=post_id)
            post.delete()
            messages.success(request, 'Пост успешно удален.')
            return redirect('/')
        except Post.DoesNotExist:
            messages.error(request, 'Пост не найден.')
            return redirect('/')
    return redirect('/')


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
            return render(request, 'main/registration.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'main/registration.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')