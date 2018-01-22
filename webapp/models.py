from django.db import models

# Create your models here.
class vehicle(models.Model):
    num_east=models.IntegerField()
    num_north=models.IntegerField()
    num_south=models.IntegerField()