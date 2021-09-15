from django.shortcuts import render
from .models import Author, Book, Owner


def index(request):
    try:
        books_list = Book.objects.all()
    except Book.DoesNotExist:
        print('error')

    return render(request, 'books/index.html', {'books_list': books_list})
