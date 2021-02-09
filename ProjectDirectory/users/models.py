from django.contrib.auth.models import AbstractUser
from django.db import models 

class CustomUser(AbstractUser):
	pass
	
	def __str__(self):
		return self.username

class Team(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	
	user = models.ForeignKey(
		'CustomUser',
		on_delete=models.CASCADE,
		related_name='teams',	
	)
	
	speed_climber=models.ForeignKey(
		'climbers.Climber',
		on_delete=models.CASCADE,
		related_name='speed_teams',
	)

	boulder_climber=models.ForeignKey(
		'climbers.Climber',
		on_delete=models.CASCADE,
		related_name='boulder_teams',
	)

	lead_climber=models.ForeignKey(
		'climbers.Climber',
		on_delete=models.CASCADE,
		related_name='lead_teams',
	)