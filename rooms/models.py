from django.db import models




# Create your models here.
class Rooms(models.Model):
    CHOICES = (
        ('LAB','LAB'),
        ('LECTURE','LECTURE')
    )
    
    room_number = models.IntegerField(unique=True)
    room_type = models.CharField(max_length=20, choices=CHOICES,)
    capcity = models.IntegerField()
   
    
    def __str__(self):
        room = self.room_number
        room = str(room)
        return room