from django.db import models
from datetime import datetime, timedelta
import dateutil.rrule as rrule

class Event(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=1000)
	type = models.CharField(max_length=100, choices=[('musique', 'Musique'), ('discussion', 'Discussion'), ('autre', 'Autre')])
	#illustration
	#hosts

	def __str__(self):
		return self.title
	
class EventInstance(models.Model):
	RECURRENCE_TYPE = [
		('ONCE', 'Ponctuelle'),
		('DAILY', 'Quotidienne'),
		('WEEKLY', 'Hebdomadaire'),
		('MONTHLY', 'Mensuelle'),
	]

	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	recurrence = models.CharField(max_length=10, choices=RECURRENCE_TYPE, default='ONCE')

	def __str__(self):
		return f"{self.event.title} ({self.recurrence})"

	def get_occurrences(self, from_date, to_date):
		if self.recurrence == 'ONCE':
			if from_date <= self.start_time <= to_date:
				return [(self.start_time, self.end_time)]
			else:
				return []

		freq_map = {
			'DAILY': rrule.DAILY,
			'WEEKLY': rrule.WEEKLY,
			'MONTHLY': rrule.MONTHLY,
		}

		freq = freq_map.get(self.recurrence)

		duration = self.end_time - self.start_time

		occurrences = list(rrule.rrule(
			freq,
			dtstart=self.start_time,
			until=to_date
		))

		return [(occ, occ + duration) for occ in occurrences if from_date <= occ <= to_date]