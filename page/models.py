from django.db import models
import datetime
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class WeeklySchedule(models.Model):
    DAY_CHOICES = [
        ('pazartesi', 'Pazartesi'),
        ('salı', 'Salı'),
        ('çarşamba', 'Çarşamba'),
        ('perşembe', 'Perşembe'),
        ('cuma', 'Cuma'),
        ('cumartesi', 'Cumartesi'),
        ('pazar', 'Pazar'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES, unique=True)
    opening_hours = models.TimeField()
    closing_hours = models.TimeField(default=datetime.time(0, 0))

    def __str__(self):
        return f"{self.day}: {self.opening_hours}"
    
    class Meta:
        ordering = ['day']

