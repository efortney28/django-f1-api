from django.db import models

# Create your models here.
class Circuit(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads/circuits/')
    turns = models.PositiveSmallIntegerField(default=0)
    total_gp = models.PositiveSmallIntegerField(default=0)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    first_gp_date = models.DateField(blank=True, null=True)
    capacity = models.IntegerField(default=0)
    length = models.FloatField(default=0.0)
    race_lap_record = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name