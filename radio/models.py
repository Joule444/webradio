from django.db import models

class Event(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	type = models.CharField(max_length=100, choices=[('musique', 'Musique'), ('event', 'Event'), ('autre', 'Autre')])

	def __str__(self):
		return self.title
	
