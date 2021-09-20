from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    # student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='category/images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('category:detail', args=[str(self.id)])
