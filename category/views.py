from django.shortcuts import render
# , CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
#from .models import Book
from category.models import Category
# Create your views here.


class CategoryListView(ListView):

    model = Category
    template_name = "category/home.html"
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category/category_detail.html"
