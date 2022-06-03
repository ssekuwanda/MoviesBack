from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesListAPIView.as_view(), name='movies'),
    path('<int:id>', views.MovieDetailAPIView.as_view(), name="movie"),
]