from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (movie_list, movie_detail,
                          GenreList, GenreDetail,
                          ActorListCreate, ActorRetrieveUpdateDestroy,
                          CinemaHallViewSet, MovieViewSet)

router = DefaultRouter()
router.register(r"cinema/movies", MovieViewSet)
router.register(r"cinema/cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("cinema/genres/", GenreList.as_view(), name="genre-list"),
    path("cinema/genres/<int:pk>/",
         GenreDetail.as_view(),
         name="genre-detail"),
    path("cinema/actors/",
         ActorListCreate.as_view(),
         name="actor-list"),
    path("cinema/actors/<int:pk>/",
         ActorRetrieveUpdateDestroy.as_view(),
         name="actor-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
