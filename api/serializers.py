from rest_framework import serializers

from viewer.models import Movie, Creator, Country, Genre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        #fields = ['title_orig', 'title_cz', 'year']
        fields = "__all__"


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        #fields = ['title_orig', 'title_cz', 'year']
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        #fields = ['title_orig', 'title_cz', 'year']
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        #fields = ['title_orig', 'title_cz', 'year']
        fields = "__all__"
