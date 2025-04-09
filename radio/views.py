import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import EventInstance
from datetime import datetime, timedelta
from django.utils.timezone import now, make_aware

def get_events(request):
	day_param = request.GET.get('day')
	today = now().date()

	if day_param is not None:
		day_index = int(day_param)
		if (day_index == 0):
			day_index = 6
		else:
			day_index -= 1
		target_day = today - timedelta(days=today.weekday() - day_index)
		start = make_aware(datetime.combine(target_day, datetime.min.time()))
		end = start + timedelta(days=1)
	else:
		start = make_aware(datetime.combine(today, datetime.min.time()))
		end = start + timedelta(days=7)

	events_list = []
	for instance in EventInstance.objects.all():
		occurrences = instance.get_occurrences(start, end)
		for occ_start, occ_end in occurrences:
			events_list.append({
				'title': instance.event.title,
				'start_time': occ_start.isoformat(),
				'end_time': occ_end.isoformat(),
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
