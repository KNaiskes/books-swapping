from django.shortcuts import render
from django.http import Http404
from .models import Author, Book, Owner


def books(request):
        books_list = Book.objects.all()
        return render(request, 'books/books.html', {'books_list': books_list})

def book_details(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')
    return render(request, 'books/book_details.html', {'book': book})

def authors(request):
    authors_list = Author.objects.all()
    return render(request, 'books/authors.html', {'authors_list': authors_list})

def author_details(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404('Author does not exist')
    return render(request, 'books/author_details.html', {'author': author})

def owners(request):
    owners_list = Owner.objects.all()
    return render(request, 'books/owners.html', {'owners_list': owners_list})

def owner_details(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404('Owner does not exist')
    return render(request, 'books/owner_details.html', {'owner': owner})

# Filter by

def books_by_author(request, author):
        try:
                books = Book.objects.filter(authors=author)
        except Author.DoesNotExist:
                books = None

        return render(request, 'books/books_by_author.html', {'books': books})
