from django import forms
from book.models import Book
from category.models import Category


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'description',  'img',
                  'category']
        categories = Category.objects.all()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'email text_box ',
                'placeholder': 'Title ',
                'id': 'title'}),
            'author': forms.TextInput(attrs={
                'class': 'email text_box ',
                'placeholder': 'Author ',
                'id': 'title'}),
            'description': forms.TextInput(attrs={
                'class': 'email text_box  ',
                'placeholder': 'Description ',
                'id': 'title'}),

            'img': forms.FileInput(attrs={
                'class': 'email text_box',
                'id': 'username'}),
            'category': forms.Select(choices=categories, attrs={'class': 'text_box  email', 'placeholder': 'Title '}),

        }
        labels = {
            'title': '',
            'author': '',
            'description': '',
            'category': '',
            'img': '',


        }
