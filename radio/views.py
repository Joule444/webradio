import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import EventInstance
from datetime import datetime, timedelta, timezone
from django.utils.timezone import make_aware

def get_events(request):
	from_date = make_aware(datetime.now(), timezone=timezone.utc)
	to_date = from_date + timedelta(days=30)

	all_instances = EventInstance.objects.all()
	events_list = []

	for instance in all_instances:
		occurrences = instance.get_occurrences(from_date, to_date)
		for start_time, end_time in occurrences:
			events_list.append({
				'title': instance.event.title,
				'start_time': start_time.isoformat(),
				'end_time': end_time.isoformat(),
			})

	events_list.sort(key=lambda x: x['start_time'])

	return JsonResponse(events_list, safe=False)

def agenda(request):
	return render(request, 'radio/agenda.html')

def get_current_song():
	url = "http://141.95.149.137:8000/status-json.xsl"

	try:
		response = requests.get(url)
		data = response.json()

		if "icestats" in data and "source" in data["icestats"]:
			source = data["icestats"]["source"]
			current_song = source.get("title", "").strip()

			if not current_song:
				current_song = "Titre inconnu"

		else:
			current_song = "Aucune musique en cours"

	except requests.exceptions.RequestException as e:
		print(f"Erreur de requete : {e}")
		current_song = "Impossible de récupérer les infos"

	return current_song

def current_song_api(request):
	current_song = get_current_song()
	return JsonResponse({'current_song': current_song})

def home(request):
	current_song = get_current_song()
	print(f"Titre récupéré : {current_song}")
	return render(request, 'radio/home.html', {'current_song': current_song})
