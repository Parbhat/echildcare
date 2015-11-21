from django.contrib import admin

from .models import GeneralEvent, ScheduledEvent

admin.site.site_header = "echildcare"

# Register your models here.

admin.site.register(GeneralEvent)
admin.site.register(ScheduledEvent)