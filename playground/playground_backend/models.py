from django.db import models
from django.contrib.auth.models import User


# Article model
# One-to-Many with User.
class Article(models.Model):
    title = models.CharField(max_length=150, blank=False)
    body = models.TextField(max_length=None, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        related_name='articles',
        on_delete=models.CASCADE)


# Comment model
# One-to-Many with Article
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE)
    comment = models.TextField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
