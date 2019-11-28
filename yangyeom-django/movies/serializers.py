from rest_framework import serializers
from .models import Genre, Movie, Review, ScoresExpected


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source='user.username')
    class Meta:
        model = Review
        fields = ['id', 'score', 'content', 'user', 'username', 'movie']


class MovieSerializers(serializers.ModelSerializer):
    review_set = ReviewSerializers(many=True)
    class Meta:
        model = Movie
        fields = ['code', 'title', 'poster_url', 'description', 'genres', 'like_users', 'watched_users', 'review_set', 'score_avg']


class GenreDetailSerializers(serializers.ModelSerializer):
    movies = MovieSerializers(many=True)
    class Meta(GenreSerializers.Meta): 
        fields = GenreSerializers.Meta.fields
        include = ['movies']


class ScoresExpectedSerializers(serializers.ModelSerializer):
    movie = MovieSerializers()
    username = serializers.CharField(read_only=True, source='user.username')
    class Meta:
        model = ScoresExpected
        fields = ['score', 'movie', 'user', 'movie', 'username']

class MovieDetailSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    class Meta:
        fields = MovieSerializers.Meta.fields
        include = ['reviews']
