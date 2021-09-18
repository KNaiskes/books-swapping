from django.shortcuts import render
from django.http import Http404
from .models import Author, Book, Owner


def index(request):
    try:
        books_list = Book.objects.all()
    except Book.DoesNotExist:
        print('error')

    return render(request, 'books/index.html', {'books_list': books_list})

def book_details(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')
    return render(request, 'books/book_details.html', {'book': book})

def authors(request):
    try:
        authors_list = Author.objects.all()
    except Author.DoesNotExist:
        print('error')
    return render(request, 'books/authors.html', {'authors_list': authors_list})

def author_details(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404('Author does not exist')
    return render(request, 'books/author_details.html', {'author': author})
