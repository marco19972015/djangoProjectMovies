from django.http import HttpResponse
from django.shortcuts import render

# 2. The view then takes a request
def movies(request):
    # 3. it then returns an Http request
    # return HttpResponse("Hello World")

    # Takes in three arguments 
    # 1. Passing along the request
    # 2. The actual template itself (this is inside a string)
    # 3. then some data (we can start with a dict)
    return render(request, 'movies/movies.html', {'movies': ['movie1', 'movie2']})

def home(request):
    return HttpResponse('Home page')