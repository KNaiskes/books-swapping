# Generated by Django 3.2.7 on 2021-10-01 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_owner_books'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('first_name', 'middle_name', 'last_name')},
        ),
    ]
