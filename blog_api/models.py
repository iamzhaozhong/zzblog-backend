from django.db import models
# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length=256)
  access_level = models.CharField(max_length=256)

  def __str__(self):
      return self.name

class Entry(models.Model):
    title = models.CharField(max_length=128)
    released = models.DateField()
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='entries')

    def __str__(self):
        return self.title
