from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Book(models.Model):
    class Meta:
        verbose_name = 'Book in book shop'
        verbose_name_plural = 'Books in book shop'

    title = models.CharField(max_length=50,
                             verbose_name='Name',
                             help_text="this is name of book"
                             )
    date = models.DateTimeField(auto_now_add=True, null=True)
    authors = models.ManyToManyField(User, related_name='books')

    def __str__(self):
        return f"{self.title}  {self.id}"


class Comment(models.Model):

    text = models.TextField('comment')
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Mark(models.Model):

    text = models.TextField('mark for book')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)



