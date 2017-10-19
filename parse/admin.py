from django.contrib import admin

from parse.models import DayHistory
# Register your models here.
class DayHistoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'date'

admin.site.register(DayHistory, DayHistoryAdmin)