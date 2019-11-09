from django.db import models
from django.contrib.auth.models import User


# Article model
# One-to-Many with User.
class Article(models.Model):
    title = models.CharField(max_length=150, blank=False)
    body = models.TextField(max_length=None, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# GuestUser model
# One-to-Many with Comment
class GuestUser(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.IntegerField(default=1)
    is_admin = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


# Comment model
# One-to-Many with Article
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
