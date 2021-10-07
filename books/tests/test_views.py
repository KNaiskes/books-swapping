from django.test import TestCase
from django.urls import reverse

from books.models import Author, Book, Owner

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        for i in range(2):
            Author.objects.create(
                first_name=f'first_name {i}',
                middle_name=f'middle_name {i}',
                last_name=f'last_name {i}',
            )


    def test_view_url_location(self):
        response = self.client.get('/books/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('books:authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('books:authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/authors.html')


class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        from datetime import date
        today = date.today()

        for i in range(2):
            Author.objects.create(
                first_name=f'first_name {i}',
                middle_name=f'middle_name {i}',
                last_name=f'last_name {i}',
            )

        book1 = Book.objects.create(
            title = 'book1',
            pub_date = today
        )
        book1.authors.add(None)

    def test_view_url_location(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('books:books'))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('books:books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')

class BooksByAuthor(TestCase):

    def test_view_url_location(self):
        response = self.client.get('/books/books_by_author/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('books:books_by_author',
                                           kwargs={'author': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books_by_author.html')
