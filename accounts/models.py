from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    joined = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile_images/',  default='profile.jpg')

    def __str__(self):
        return self.username
    
    #def get_absolute_url(self):
    #    return reverse('user_detail', args=[str(self.id)])