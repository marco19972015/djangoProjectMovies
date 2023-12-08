# Remember when making a change we have to tell django that there was a change 
from django.db import models

# To create the table (structure we inherit from Model class)
class Movie(models.Model):
    # the code below will return us a Movie object (1) on our view
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    # to get the actual movie we override __str__(self) method
    # self is taken as an arugment to refer to the attributes in the class
    def __str__(self):
        return f'{self.title} from {self.year}'

