from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# , CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Book
from category.models import Category
# Create your views here.


class BookListView(ListView):

    model = Book
    template_name = "book/home.html"
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[
            :5]
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book_detail.html"


class BorrowBtn(View):
    template_name = 'book/home.html'

    def post(self, request,  * args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        book.return_date = request.POST["return_date"]
        book.status = 'Borrowed'
        book.save()
        return redirect('book:book_detail', kwargs['pk'])

    def get(self, request, *args, **kwargs):

        return redirect('book:book')


class ReturnBtn(View):

    def post(self, request,  * args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        book.return_date = None
        book.status = 'Available'
        book.save()
        return redirect('book:book_detail', kwargs['pk'])

    def get(self, request, *args, **kwargs):

        return redirect('book:book')


class Search(View):

    def post(self, request,  * args, **kwargs):
        searchname = request.POST["search"]
        if searchname == '':
            return redirect('book:book')
        books = Book.objects.filter(title__startswith=searchname)
        books = books | Book.objects.filter(author__startswith=searchname)

        return render(request, 'book/search.html', {'books': books})

    def get(self, request, *args, **kwargs):

        return redirect('book:book')
