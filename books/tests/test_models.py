from django.test import TestCase
from books.models import Author, Book, Owner

class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(
            first_name='Author1', middle_name='M1',last_name='AuthLast1'
        )

        Author.objects.create(
            first_name='Author2', middle_name='M2',last_name='AuthLast2'
        )

    def test_str(self):
        author1 = Author.objects.get(id=1)
        author2 = Author.objects.get(id=2)

        self.assertEqual(
            str(author1), '%s %s' % (author1.first_name,author1.last_name)
        )

        self.assertEqual(
            str(author2), '%s %s' % (author2.first_name,author2.last_name)
        )


class BookTestCase(TestCase):
    def setUp(self):
        from datetime import date
        today = date.today()

        author1 = Author.objects.create(
            first_name='Author1', middle_name='M1',last_name='AuthLast1'
        )

        author2 = Author.objects.create(
            first_name='Author2', middle_name='M2',last_name='AuthLast2'
        )

        book1 = Book.objects.create(title='title_book1', pub_date=today)
        book1.authors.add(author1)

        book2 = Book.objects.create(title='title_book2', pub_date=today)
        book2.authors.add(author2)

    def test_str(self):
        author1 = Author.objects.get(id=1)
        author2 = Author.objects.get(id=2)

        book1 = Book.objects.get(id=1)
        book2 = Book.objects.get(id=2)

        self.assertEqual(
            str(book1), '%s' % (book1.title)
        )

        self.assertEqual(
            str(book2), '%s' % (book2.title)
        )
