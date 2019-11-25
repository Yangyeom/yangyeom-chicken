from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Movie API",
      default_version='v1',
      description="Movie Info"
   ),
)

app_name = 'movies'

urlpatterns = [
    path('movies/', views.movies_index, name='movies_index'),
    path('movies/<int:movie_pk>/', views.movie_reviews, name='movie_reviews'),
    path('<int:movie_pk>/reviews/new/', views.review_create, name='review_create'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('recommend/', views.recommend, name="recommend"),

    path('redoc/', schema_view.with_ui('redoc')),
    path('swagger/', schema_view.with_ui('swagger')),
]