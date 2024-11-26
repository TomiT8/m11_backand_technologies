from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, FormView, UpdateView, DeleteView

from viewer.forms import CreatorForm, MovieForm, GenreForm, CountryForm
from viewer.models import Movie, Creator, Genre, Country


def home(request):
    return render(request, "home.html")


def movies(request):
    return render(request,
                  "movies.html",
                  {'movies': Movie.objects.all(),
                   'genres': Genre.objects.all(),
                   'countries': Country.objects.all()})


class MoviesView(View):
    def get(self, request):
        return render(request,
                      "movies.html",
                      {'movies': Movie.objects.all(),
                       'genres': Genre.objects.all(),
                       'countries': Country.objects.all()})


class MoviesTemplateView(TemplateView):
    template_name = "movies.html"
    extra_context = {'movies': Movie.objects.all(), 'genres': Genre.objects.all(), 'countries': Country.objects.all()}


class MoviesListView(ListView):
    template_name = "movies.html"
    model = Movie


def movie(request, pk):
    try:
        return render(request, "movie.html", {'movie': Movie.objects.get(id=pk)})
    except:
        return home(request)


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    model = Movie
    permission_required = 'viewer.change_movie'


    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'



class CreatorsListView(ListView):
    template_name = "creators.html"
    model = Creator


def creator(request, pk):
    try:
        return render(request, "creator.html", {'creator': Creator.objects.get(id=pk)})
    except:
        return home(request)


class CreatorFormView(FormView):
    template_name = "form.html"
    form_class = CreatorForm
    success_url = reverse_lazy('creators')

    def form_valid(self, form):
        print("Form is valid")
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Creator.objects.create(
            first_name=cleaned_data["first_name"],
            last_name=cleaned_data["last_name"],
            date_of_birth=cleaned_data["date_of_birth"],
            date_of_death=cleaned_data["date_of_death"],
            nationality=cleaned_data["nationality"],
            biography=cleaned_data["biography"]
        )
        return result

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CreatorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CreatorForm
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.add_creator'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CreatorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CreatorForm
    success_url = reverse_lazy('creators')
    model = Creator
    permission_required = 'viewer.change_creator'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CreatorDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Creator
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.delete_creator'


class GenreListView(ListView):
    template_name = "genres.html"
    model = Genre


def genre(request, pk):
    try:
        return render(request, "genre.html", {'genre': Genre.objects.get(id=pk)})
    except:
        return home(request)


class GenreFormView(FormView):
    template_name = "form.html"
    form_class = GenreForm
    success_url = reverse_lazy('genres')

    def form_valid(self, form):
        print("Form is valid")
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Genre.objects.create(
            name=cleaned_data["name"]
        )
        return result

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class GenreCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.add_genre'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genres')
    model = Genre
    permission_required = 'viewer.change_genre'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Genre
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.delete_genre'


class CountryListView(ListView):
    template_name = "countries.html"
    model = Country


def country(request, pk):
    try:
        return render(request, "country.html", {'country': Country.objects.get(id=pk)})
    except:
        return home(request)


class CountryFormView(FormView):
    template_name = "form.html"
    form_class = CountryForm
    success_url = reverse_lazy('countries')

    def form_valid(self, form):
        print("Form is valid")
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Country.objects.create(
            name=cleaned_data["name"]
        )
        return result

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CountryCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CountryForm
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.add_country'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CountryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CountryForm
    success_url = reverse_lazy('countries')
    model = Country
    permission_required = 'viewer.change_country'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CountryDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Country
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.delete_country'
