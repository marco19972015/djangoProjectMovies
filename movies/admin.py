# Here we describe what tables we want to show up in our admin site
from .models import Movie

# The line below allows us to get a reference to the admin page
from django.contrib import admin

# using admin.site.register is how we add our Movie model to the admin page
# NOTE this will execute on server startup
admin.site.register(Movie)