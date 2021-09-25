from django.urls import path
from .views import BookCreateView, BookUpdateView, BookDeleteView

app_name = 'myadmin'
urlpatterns = [
    path('add_book/', BookCreateView.as_view(), name="add_book"),
    path('edit_book/<int:pk>/', BookUpdateView.as_view(), name="edit_book"),
    path('delete_book/<int:pk>/', BookDeleteView.as_view(), name="delete_book"),


]
