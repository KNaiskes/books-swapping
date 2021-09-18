from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.book_details, name='book_details'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author_details, name='author_details'),
    path('owners/', views.owners, name='owners'),
]
