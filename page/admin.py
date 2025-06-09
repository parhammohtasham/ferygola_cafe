from django.contrib import admin
from .models import WeeklySchedule , Contact
# Register your models here.
@admin.register(WeeklySchedule)
class WeeklyScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 'opening_hours', 'closing_hours')
    ordering = ('day',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
