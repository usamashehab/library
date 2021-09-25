from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    img = models.ImageField(upload_to='student/images/',
                            default='static/accounts/images/profile.jpg')
