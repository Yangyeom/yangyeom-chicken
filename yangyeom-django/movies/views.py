from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from math import sqrt
from django.contrib.auth import get_user_model
from accounts.models import Similarity

from .models import Movie, Genre, Review
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import MovieSerializers, ReviewSerializers
from rest_framework.response import Response


# def index(request):
#     return render(request, 'movies/index.html', {'movies': Movie.objects.all()})
@api_view(['GET'])
@permission_classes([AllowAny])
def movies_index(request):
    """
    영화 정보
    """
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movies_rating(request):
    """
    평가할 영화 정보
    """
    movies = Movie.objects.all()[:30]
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

# def detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     form = ReviewForm()
#     reviews = movie.review_set.all()
#     return render(request, 'movies/detail.html', {'movie': movie, 'form': form, 'reviews': reviews, })
# @api_view(['GET'])
# def detail(request, movie_pk):
#     """
#     영화 상세 정보
#     """
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieSerializers(movie)
#     return Response(serializer.data)
# # ===================================================================================================
# @api_view(['GET', 'POST'])
# def todo_index_create(request):
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializers = TodoSerializers(todos, many=True)
#         return Response(serializers.data)
#     else:
#         # request.POST : FormData로 POST 전송할 때 여기에 값이 들어있음
#         # request.data : FormData로 POST 전송할 경우와 data로 전송할 경우 둘다 여기에 값이 들어있음
#         serializers = TodoSerializers(data=request.data)
#         if serializers.is_valid(raise_exception=True):  # 잘못된 요청이 오면 해당 오류 메세지가 뜰 거임
#             serializers.save()
#             return Response(serializers.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def movie_reviews(request, movie_pk):
    if request.method == 'GET':
        print('영화 정보 가져오기', request.user)
        rated = False
        reviews = Review.objects.filter(movie_id=movie_pk)
        # for review in reviews:
        #     if request.user == review.user:
        #         rated = True
        #         break
        serializers = ReviewSerializers(reviews, many=True)
        # serializers.data.append(rated)
        # print('serializers', serializers.data)
        return Response(serializers.data)
    else:
        print("****데이터:", request.data)
        serializer = ReviewSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            review = serializer.save()
            review.movie.watched_users.add(review.user)
            print('요청 보내짐')
            return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def review_update_delete(request, movie_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    print(request.user)
    print(review.user)
    if request.user == review.user:
        if request.method == 'PUT':
            pass
        else:
            print('요청받음')
            print(request.user)
            
            review.delete()
            return Response('삭제되었습니다')
    else:
        return Response('리뷰 작성자가 아닙니다.')


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
def evaluate_Simi(request):  # 가입할 때마다!
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


@login_required
def recommend(request):
    user_now = request.user
    movies_recom = []
    for movie in Movie.objects.all():
        if movie in user_now.watched_movies.all(): continue
        score_expected = 0; summ_similarity = 0
        for user in get_user_model():
            if user == user_now: continue
            if movie in user.watched_movies.all():
                similarity = Similarity.objects.filter(reference_user=user_now, similar_user=user).similarity
                if similarity > 0:
                    summ_similarity += similarity
                    score_expected += similarity * Review.objects.filter(user=user, movie=movie).score
        score_expected /= summ_similarity
        movies_rocom.append((movie, score_expected))
    movies.sort(key=lambda x: x[1], reverse=True)
    return movies[:10]