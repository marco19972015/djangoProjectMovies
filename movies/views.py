from django.http import HttpResponse, HttpResponseRedirect
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

# This add view will be the page used when we add a movie
# But, it will also be the view that accepts the data that's typed in here
def add(request):
    # This is a POST request, meaning the information is sent with the request body
    # This can be seen in dev tools 
    title = request.POST.get('title')
    year = request.POST.get('year')

    # if title and year have values 
    if title and year:
        # Create a movie object = new Movie(title is equal to title coming in, and year is equal to year coming in)
        movie = Movie(title=title, year=year)
        # we then invoke movie.save() to save to the database
        movie.save()
        # we now re-direct back to the list of movies template
        return HttpResponseRedirect('/movies')
    
    return render(request, 'movies/add.html')



    # In our dev tools we navigate to the Network tab, in our waterfall we can see add being sent
    # In the headers tag we can see the URL 
    # Payload is what we actually sent
        # This contains two things 
        # title: 
        # year: 
    # So to get the data from our payload we write request.POST
    # Since it's a dictionary we can use .get to access any element 