from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Genre, Review
from .forms import ReviewForm
from math import sqrt
from django.contrib.auth import get_user_model
import sys
sys.path.append("..")
from accounts.models import Similarity

# Create your views here.
def index(request):
    return render(request, 'movies/index.html', {'movies': Movie.objects.all()})


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm()
    reviews = movie.review_set.all()
    return render(request, 'movies/detail.html', {'movie': movie, 'form': form, 'reviews': reviews, })


@login_required
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
            movie.score_sum += comment.score
            movie.score_avg = round(movie.score_sum / max(movie.review_set.count(), 1), 2)
            movie.save()
            return redirect('movies:detail', movie_pk)
        else:
            return redirect('movies.detail', movie_pk)


def review_delete(request, movie_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user: 
        movie = Movie.objects.get(pk=movie_pk)
        movie.score_sum -= review.score
        review.delete()
        movie.score_avg = round(movie.score_sum / max(movie.review_set.count(), 1), 2)
        movie.save()
    return redirect('movies:detail', movie_pk)


@login_required
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:detail', movie_pk)

@login_required
def rate(request):
    user_now = request.user
    for user in get_user_model().objects.all():
        if user == user_now: continue
        cnt_same_movie = 0
        for movie in user.watched_movies.all():
            if movie in user_now.watched_movies.all():
                cnt_same_movie += 1
        if cnt_same_movie >= 3:
            numerator = 0; sigma_user = 0; sigma_user_now = 0
            for movie in user.watched_movies.all():
                if movie in user_now.watched_movies.all():
                    numerator += (Review.objects.filter(movie=movie, user=user)[0].score - user.score_avg)\
                                    * (Review.objects.filter(movie=movie, user=user_now)[0].score - user_now.score_avg)
                    sigma_user += (Review.objects.filter(movie=movie, user=user)[0].score - user.score_avg) ** 2
                    sigma_user_now += (Review.objects.filter(movie=movie, user=user_now)[0].score - user_now.score_avg) ** 2
            sigma_user = sqrt(sigma_user); sigma_user_now = sqrt(sigma_user_now)
            similarity = numerator / (sigma_user * sigma_user_now)
            Similarity.objects.create(reference_user=user_now, similar_user=user, similarity=similarity)
            Similarity.objects.create(reference_user=user, similar_user=user_now, similarity=similarity)