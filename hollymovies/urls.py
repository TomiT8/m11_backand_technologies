"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from accounts.views import SubmittableLoginView, SignUpView, user_logout
from api.views import Movies, MovieDetail, Creators, CreatorDetail, CountryDetail, Countries, Genres, GenreDetail
from hollymovies import settings
from viewer.models import Movie

"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from viewer.views import home, movie, creator, genre, MoviesListView, \
    CreatorsListView, CreatorCreateView, CreatorUpdateView, CreatorDeleteView, country, \
    MovieUpdateView, MovieDeleteView, MovieCreateView, GenreListView, GenreCreateView, GenreUpdateView, GenreDeleteView, CountryListView, CountryCreateView, \
    CountryDeleteView, CountryUpdateView, MovieTemplateView, MoviesTemplateView, ImageDetailView, ImageCreateView, ImageUpdateView, ImageDeleteView, search

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('movies/', MoviesTemplateView.as_view(), name='movies'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/<pk>/', MovieTemplateView.as_view(), name='movie'),

    path('creators/', CreatorsListView.as_view(), name='creators'),
    path('creator/create/', CreatorCreateView.as_view(), name='creator_create'),
    path('creator/update/<pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('creator/delete/<pk>/', CreatorDeleteView.as_view(), name='creator_delete'),
    path('creator/<pk>/', creator, name='creator'),

    path('genres/', GenreListView.as_view(), name='genres'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<pk>/', GenreDeleteView.as_view(), name='genre_delete'),
    path('genre/<pk>/', genre, name='genre'),

    path('countries/', CountryListView.as_view(), name='countries'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/update/<pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<pk>/', CountryDeleteView.as_view(), name='country_delete'),
    path('country/<pk>/', country, name='country'),

    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/logout/', user_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('image/create/', ImageCreateView.as_view(), name='image_create'),
    path('image/update/<pk>/', ImageUpdateView.as_view(), name='image_update'),
    path('image/delete/<pk>/', ImageDeleteView.as_view(), name='image_delete'),
    path('image/<pk>/', ImageDetailView.as_view(), name='image'),

    path('search/', search, name='search'),

    path('api/movies/', Movies.as_view(), name='api.movies'),
    path('api/movie/<pk>/', MovieDetail.as_view(), name='api.moviedetail'),
    path('api/creators/', Creators.as_view(), name='api.creators'),
    path('api/creator/<pk>/', CreatorDetail.as_view(), name='api.creatordetail'),
    path('api/countries/', Countries.as_view(), name='api.countries'),
    path('api/country/<pk>/', CountryDetail.as_view(), name='api.countrydetail'),
    path('api/genres/', Genres.as_view(), name='api.genres'),
    path('api/genre/<pk>/', GenreDetail.as_view(), name='api.genredetail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
