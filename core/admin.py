from django.contrib import admin
from .models import WeatherData


@admin.register(WeatherData)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['city', 'period', 'date_time']
