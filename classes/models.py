from django.db import models

# Create your models here.
class Classes(models.Model):
    SUBJECTS = (
        ('CSIS','CSIS'),
        ('CSCI','CSCI'),
        ('INFO','INFO'),
        ('CIS','CIS'),

    )

    YN = (
        ('Y','YES'),
        ('N','NO'),
    )

    GRAD = (
        ('UNGR', 'Undergraduate'),
        ('GRAD', 'Graduate'),
    )

    name = models.CharField(max_length=100, unique=True)
    course_number = models.IntegerField(unique=True)
    subject = models.CharField(max_length=20,choices=SUBJECTS)
    min_hours = models.IntegerField()
    max_hours = models.IntegerField()
    fixed_hours = models.IntegerField(default=0)
    special = models.CharField(max_length=1,choices=YN,default='N')
    grad_type = models.CharField(max_length=20, choices=GRAD)
    def __str__(self):
        return self.name