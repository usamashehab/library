from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from book.models import Book
from django import forms

from student.models import CustomUser
from category.models import Category
# Create your views here.


class BookCreateView(CreateView):
    model = Book
    template_name = "myadmin/add_book.html"
    fields = ['title', 'author', 'description', 'category', 'img']


class BookUpdateView(UpdateView):
    model = Book
    template_name = "myadmin/edit_book.html"
    fields = ['title', 'author', 'description', 'category', 'img']
    widgets = {
        'title': forms.TextInput(attrs={
            'class': 'name ',
            'placeholder': 'First Name',
            'id': 'username'}),
    }


class BookDeleteView(DeleteView):
    model = Book
    template_name = "myadmin/delete_book.html"
    success_url = reverse_lazy('book:book')
