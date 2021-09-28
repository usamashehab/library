from django.urls import path
from .views import HomeListView, BookDetailView, BorrowBtn, ReturnBtn, Search, BookListView
app_name = 'book'
urlpatterns = [
    path('', HomeListView.as_view(), name='book'),
    path('books/', BookListView.as_view(), name='list_book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('borrow/<int:pk>', BorrowBtn.as_view(), name='book_borrow'),
    path('return/<int:pk>', ReturnBtn.as_view(), name='book_return'),
    path('search/', Search.as_view(), name='search'),



]
