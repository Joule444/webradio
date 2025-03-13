import requests
from django.shortcuts import render

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

	except requests.exception.RequestException as e:
		print(f"Erreur de requete : {e}")
		current_song = "Impossible de récupérer les infos"

	return current_song

def home(request):
	current_song = get_current_song()
	print(f"Titre récupéré : {current_song}")
	return render(request, 'radio/home.html', {'current_song': current_song})
