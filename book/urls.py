from django.urls import path
from .views import BookListView, BookDetailView, BorrowBtn, ReturnBtn, Search
app_name = 'book'
urlpatterns = [
    path('', BookListView.as_view(), name='book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('borrow/<int:pk>', BorrowBtn.as_view(), name='book_borrow'),
    path('return/<int:pk>', ReturnBtn.as_view(), name='book_return'),
    path('search/', Search.as_view(), name='search'),



]
