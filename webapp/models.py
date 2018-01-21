from django.db import models

# Create your models here.
class vehicle(models.Model):
    num_east=models.IntegerField()
    north_east = models.IntegerField()
    south_east = models.IntegerField()