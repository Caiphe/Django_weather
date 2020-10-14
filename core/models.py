from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=25)
    period = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.city + ' ' + self.period

    class Meta:
        verbose_name_plural = 'Weather Data'