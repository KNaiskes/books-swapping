from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:book_id>/', views.book_details, name='book_details'),
    path('authors/', views.authors, name='authors'),
]
