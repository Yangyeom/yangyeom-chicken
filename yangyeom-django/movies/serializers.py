from rest_framework import serializers
from .models import Genre, Movie, Review


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    # username = serializers.CharField(read_only=True, source='user.username')
    class Meta:
        model = Review
        fields = ['score', 'content', 'user', 'movie']



class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreDetailSerializers(serializers.ModelSerializer):
    movies = MovieSerializers(many=True)
    class Meta(GenreSerializers.Meta): 
        fields = GenreSerializers.Meta.fields
        include = ['movies']

# class MovieDetailSerializers(serializers.ModelSerializer):
#     reviews = ReviewSerializers(many=True)
#     class Meta:
#         fields = MovieSerializers.Meta.fields
#         include = ['reviews']
