from django.db import models

from classes.models import Classes
from rooms.models import Rooms

# Create your models here.
class Scheduled(models.Model):
    course = models.ForeignKey(Classes, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    start_time = models.IntegerField(blank=True)
    end_time = models.IntegerField(blank=True)
    flex = models.IntegerField(default=1)
    crn = models.IntegerField()
    offering = models.IntegerField()
    name = models.CharField(max_length=100, blank=True)
    banner_id = models.CharField(max_length=100, blank=True)
    primary = models.CharField(max_length=100, blank=True)
    monday = models.CharField(max_length=1, blank=True)
    tuesday = models.CharField(max_length=1, blank=True)
    wednesday = models.CharField(max_length=1, blank=True)
    thursday = models.CharField(max_length=1,  blank=True)
    friday = models.CharField(max_length=1, blank=True)
    saturday = models.CharField(max_length=1,  blank=True)
    sunday = models.CharField(max_length=1, blank=True)
    building = models.CharField(max_length=5,default='8')   
    campus = models.CharField(max_length=5,default='M')
    delivery = models.CharField(max_length=2, default='TR')
    notes = models.CharField(max_length=200, blank=True)
    capacity = models.IntegerField(blank=True)
    def __str__(self):
        return self.course.name
