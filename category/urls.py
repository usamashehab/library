from django.urls import path
from .views import CategoryListView, CategoryDetailView
app_name = 'category'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='detail'),


]
