# Remember when making a change we have to tell django that there was a change 
from django.db import models

# To create the table (structure we inherit from Model class)
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
