from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    img = models.ImageField(upload_to='student/images/',
                            default='../static/accounts/images/profile.jpg')

    def get_absolute_url(self):  # new
        return reverse('std_profile', args=[str(self.id)])
