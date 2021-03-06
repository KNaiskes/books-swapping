from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, default='')
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']
        unique_together = ('first_name', 'middle_name', 'last_name')

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    pub_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        unique_together = ('title', 'pub_date')

class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, unique=True)
    books = models.ManyToManyField(Book)
    photo = models.ImageField(upload_to='owners_images')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']
        unique_together = ('last_name', 'email')
