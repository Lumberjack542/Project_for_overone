from django.db import models

# Create your models here.


class Planer(models.Model):
    title = models.TextField(max_length=150, verbose_name='Название', help_text='this is name of planer')
    data = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to="media/image")

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Planer, on_delete=models.CASCADE, related_name='comments')