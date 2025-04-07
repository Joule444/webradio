import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Event

def get_events(request):
	events = Event.objects.all()
	events_list = []
	for event in events:
		events_list.append({
			'title': event.title,
			'start_time': event.start_time.isoformat(),
			'end_time': event.end_time.isoformat(),
		})
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
