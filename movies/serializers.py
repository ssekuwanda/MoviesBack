from rest_framework import serializers
from .models import Movie, Downloaded

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description','image','file', )
        model = Movie

class DownloadedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'movie' )
        model = Downloaded