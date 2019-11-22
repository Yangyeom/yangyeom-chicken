from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import sys
sys.path.append("..")
from movies.models import Movie

def index(request):
    context = {
        'users' : get_user_model().objects.all()
    }
    return render(request, 'accounts/index.html', context)

def detail(request, user_pk):
    context = {
        'user_detail' : get_user_model().objects.get(pk=user_pk)
    }
    return render(request, 'accounts/detail.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')  # 홈화면으로 돌리기
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect('accounts:rating')  # 홈화면으로 돌리기
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')  # 홈화면으로 돌리기
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')  # 홈 화면으로 돌리기
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')  # 홈화면으로 돌리기

@login_required
def follow(request, user_detail_pk):
    user_detail = get_object_or_404(get_user_model(), pk=user_detail_pk)
    user = request.user
    if user != user_detail:
        if user in user_detail.followers.all():
            user_detail.followers.remove(user)
        else:
            user_detail.followers.add(user)
    return redirect('accounts:detail', user_detail_pk)


def rating(request):
    movies = Movie.objects.all()[:30]
    context = {
        'movies': movies
    }
    return render(request, 'accounts/rating.html', context)



def display(request):
    print(request.GET)
