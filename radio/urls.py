from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('current-song/', views.current_song_api, name='current_song_api'),
	path('programme/', views.programme, name='programme'),
	path('api/events/', views.get_events, name='get_events'),
]