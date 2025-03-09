from django.db import models

# Create your models here.
class Weather_search(models.Model):
    city = models.CharField(max_length = 100)
    weather_info = models.TextField()
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.searched_at}"