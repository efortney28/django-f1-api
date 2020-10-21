from django.db import models


# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.DateField()
    country = models.CharField(max_length=200)
    championships = models.PositiveSmallIntegerField()
    total_wins = models.PositiveIntegerField(default=0)
    podiums = models.PositiveIntegerField(default=0)
    current_driver = models.BooleanField()
    career_points = models.IntegerField(default=0)
    season_points = models.IntegerField(blank=True, default=0)
    season_team = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/drivers')
    description = models.TextField(blank=True, null=True)
    car_number = models.IntegerField(default=0)
    entries = models.IntegerField(default=0)
    pole_positions = models.IntegerField(default=0)
    fastest_laps = models.IntegerField(default=0)


    def __str__(self):
        return self.name

