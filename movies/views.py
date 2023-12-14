from django.http import HttpResponse
from django.shortcuts import render

# we import Movie from .models to access the objects within
from .models import Movie

# The view then takes a request
def movies(request):

    # We assing the method to variable data to refer to all the movie objects 
    data = Movie.objects.all()

    # Takes in three arguments 
    return render(request, 'movies/movies.html', {'movies': data})

# Returns the home view
def home(request):
    return HttpResponse('Home page')
 
# we pass 'id' as extra data to this view
def detail(request, id):
    # We can ask for a certain primary key based on pk and id
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})