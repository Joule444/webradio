from django.urls import path
from . import views
from .views import home, current_song_api

urlpatterns = [
	path('', views.home, name='home'),
	path('current-song/', current_song_api, name='current_song_api'),
	path('agenda/', views.agenda, name='agenda'),
	path('api/events/', views.get_events, name='get_events'),
]