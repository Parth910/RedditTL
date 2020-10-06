from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Auth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    refresh_token = models.TextField()


class Subreddit(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.TextField()

    @classmethod
    def create(cls, name):
        author = cls(name=name)
        # do something with the book
        return author


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.TextField()
    post_title = models.TextField()
    post_subreddit = models.TextField()
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_text = models.TextField()
    link_contain = models.BooleanField(null=True)


class Domain(models.Model):
    name = models.TextField()
    post = models.ManyToManyField(Post)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

