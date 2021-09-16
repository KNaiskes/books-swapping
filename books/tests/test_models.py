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
