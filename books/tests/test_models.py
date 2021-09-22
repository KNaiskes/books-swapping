from django.test import TestCase
from books.models import Author, Book, Owner

class ModelsMixin(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(
            first_name='Author1', middle_name='M1',last_name='AuthLast1'
        )

        self.author2 = Author.objects.create(
            first_name='Author2', middle_name='M2',last_name='AuthLast2'
        )


class AuthorTestCase(ModelsMixin):
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


class OwnerTestCase(TestCase):
    def setUp(self):
        owner1 = Owner.objects.create(
            first_name='owner1',
            last_name='owner1_last', email='owner1@email.com'
        )
        owner1.books.add(None)

    def test_str(self):
        owner1 = Owner.objects.get(id=1)

        self.assertEqual(
            str(owner1), '%s %s' % (owner1.first_name, owner1.last_name)
        )
