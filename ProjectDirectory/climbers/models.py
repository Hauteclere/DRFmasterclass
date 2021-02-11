from django.db import models

class Climber(models.Model):

    name = models.CharField(max_length=100)

    class Specialties(models.TextChoices):
        SPEED = 'S', 'Speed'
        LEAD = 'L', 'Lead'
        BOULDER = 'B', 'Boulder'
    
    specialty = models.CharField(
        max_length=1,
        choices=Specialties.choices,
    )