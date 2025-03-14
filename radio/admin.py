from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'start_time', 'end_time', 'type')
	list_filter = ('type',)
	search_fields = ('type',)

admin.site.register(Event, EventAdmin)
