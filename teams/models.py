from django.db import models
from drivers.models import Driver

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='uploads/constructors')
    founded = models.DateField()
    current = models.BooleanField()
    season_driver1 = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='first_driver')
    season_driver2 = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='second_driver')
    season_points = models.IntegerField(blank=True)
    total_points = models.IntegerField(default=0)
    total_wins = models.PositiveIntegerField(default=0)
    total_titles = models.PositiveIntegerField(default=0)
    base = models.CharField(max_length=300)
    races_entered = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name
