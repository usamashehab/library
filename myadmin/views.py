from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # new
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from book.models import Book
from django import forms
from .forms import CreateBookForm, CreateCategoryForm
from student.models import CustomUser
from category.models import Category
# Create your views here.


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = "myadmin/add_book.html"

    def test_func(self):
        return self.request.user.is_staff


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = CreateBookForm
    template_name = "myadmin/edit_book.html"

    def test_func(self):
        return self.request.user.is_staff


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = "myadmin/delete_book.html"
    success_url = reverse_lazy('book:book')

    def test_func(self):
        return self.request.user.is_staff


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "myadmin/add_Category.html"

    def test_func(self):
        return self.request.user.is_staff


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "myadmin/edit_Category.html"

    def test_func(self):
        return self.request.user.is_staff


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = "myadmin/delete_Category.html"
    success_url = reverse_lazy('book:book')

    def test_func(self):
        return self.request.user.is_staff
