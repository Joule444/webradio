from django.contrib import admin
from .models import Event, EventInstance

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'type')
	list_filter = ('type',)
	search_fields = ('type',)

class EventInstanceAdmin(admin.ModelAdmin):
	list_display = ('event', 'start_time', 'end_time', 'recurrence')

admin.site.register(Event, EventAdmin)
admin.site.register(EventInstance, EventInstanceAdmin)
