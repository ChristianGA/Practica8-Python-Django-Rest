from django.contrib.auth.models import User
from django.db import models

class Categoria (models.Model):

    name = models.CharField(max_length=50)
    surname = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Post (models.Model):

    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=400)
    body = models.TextField()
    image = models.URLField(blank=True, null=True)
    publication_date = models.DateTimeField()

    create_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

    category = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title