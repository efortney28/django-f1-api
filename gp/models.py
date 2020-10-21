from django.db import models
from circuits.models import Circuit
from drivers.models import Driver
from teams.models import Team

# Create your models here.
class GP(models.Model):
    name = models.CharField(max_length=300)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    winning_driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name="winning_driver", blank=True, null=True)
    winning_constructor = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="winnging_constructor", blank=True, null=True)
    second_place_driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name="second_place_driver", blank=True, null=True)
    third_place_driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name="third_place_driver", blank=True, null=True)
    laps = models.IntegerField(default=0)

    def __str__(self):
        return self.name