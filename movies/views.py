from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import permissions
from rest_framework.permissions import IsAuthenticated


class MoviesListAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    # permission_classes = (permissions.IsOwner,IsAuthenticated)

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_fields = "id"