
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from category.models import Category
from config import settings
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    # student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="books", null=True)
    student = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, related_name="books", null=True, blank=True)
    description = models.TextField()
    img = models.ImageField(upload_to='book/images/')
    status = models.CharField(
        max_length=10,
        choices=[
            ("Available", "a"),
            ("Borrowed", "b")
        ], default="Available"
    )
    return_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('book:book_detail', args=[str(self.id)])
