from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
# from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
# from .models import User
from movies.models import Movie, Review
from django.db.models import Avg
from .serializers import UserSerializers
from rest_framework.response import Response


def index(request):
    context = {
        'users' : get_user_model().objects.all()
    }
    return render(request, 'accounts/index.html', context)

@api_view(['GET'])
def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    serializer = UserSerializers(user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')  # 홈화면으로 돌리기
    if request.method == 'POST':
        user_check = get_user_model().objects.filter(username = request.data['username']).count()
        if user_check == 0:
            get_user_model().objects.create_user(username=request.data['username'], password=request.data['password'])
            return HttpResponse('Saved', status=201)
    return HttpResponse('Unauthorized', status=401)

# def login(request):
#     if request.user.is_authenticated:
#         return redirect('accounts:index')  # 홈화면으로 돌리기
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect(request.GET.get('next') or 'accounts:index')  # 홈 화면으로 돌리기
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'accounts/form.html', context)

# def logout(request):
#     auth_logout(request)
#     return redirect('accounts:index')  # 홈화면으로 돌리기

# @login_required
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
    if request.method == 'GET':
        movies = Movie.objects.all()[:30]
        context = {
            'movies': movies
        }
        return render(request, 'accounts/rating.html', context)
    elif request.method == 'POST':
        # user = get_user_model()
        rate_score = 0
        rate_cnt = 0
        for k in request.POST:
            if k == 'csrfmiddlewaretoken':
                continue
            if request.POST[k] == '0':
                continue
            # rate_score += int(request.POST[k])
            # rate_cnt += 1
            movie = get_object_or_404(Movie, pk=k)
            review = Review(user=request.user, movie=movie, score=request.POST[k])
            review.save()
        # request.user.score_total = rate_score
        # request.user.score_avg = rate_score / rate_cnt
        request.user.score_avg = Review.objects.filter(user=request.user).aggregate(Avg('score')).get('score__avg')
        request.user.save()
        
        return redirect('movies:index')
