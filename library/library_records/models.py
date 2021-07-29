from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

class BookStatus(models.Model):
    book_status_choices = [('Rented', 'Rented'),
                           ('Not-Rented', 'Not-Rented')]


    status = models.CharField(max_length=50, choices=book_status_choices)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    issued_by = models.OneToOneField(Staff, on_delete=models.CASCADE)
    issued_to = models.OneToOneField(Member, on_delete=models.CASCADE)

    def __str__(self):
        return "Book Status"