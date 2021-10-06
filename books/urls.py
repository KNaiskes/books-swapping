from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:book_id>/', views.book_details, name='book_details'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author_details, name='author_details'),
    path('owners/', views.owners, name='owners'),
    path('owners/<int:owner_id>/', views.owner_details, name='owner_details'),

    path('books_by_author/<int:author>/', views.books_by_author, name='books_by_author'),
]
