from django.db import models
from drivers.models import Driver
from gp.models import GP
from teams.models import Team

# Create your models here.
class Season(models.Model):
    year = models.CharField(max_length=4)
    race1 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race1', null=True)
    race2 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race2', null=True)
    race3 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race3', null=True)
    race4 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race4', null=True)
    race5 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race5', null=True)
    race6 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race6', null=True)
    race7 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race7', null=True)
    race8 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race8', null=True)
    race9 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race9', null=True)
    race10 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race10', null=True)
    race11 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race11', null=True)
    race12 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race12', null=True)
    race13 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race13', null=True)
    race14 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race14', null=True)
    race15 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race15', null=True)
    race16 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race16', null=True)
    race17 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race17', null=True)
    race18 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race18', null=True)
    race19 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race19', null=True)
    race20 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race20', null=True)
    race21 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race21', null=True)
    race22 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race22', null=True)
    race23 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race23', null=True)
    race24 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race24', null=True)
    race25 = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, related_name='race25', null=True)
    wdc = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, blank=True, null=True)
    wcc = models.ForeignKey(Team, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return (self.year + ' season')