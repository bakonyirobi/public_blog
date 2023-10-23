from django.db import models
from django.contrib.auth.models import User
from storages.backends.s3boto3 import S3Boto3Storage


class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.SlugField()
    body = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default-movie.jpg', blank=False, storage=S3Boto3Storage(),
                              help_text="For thumb please upload an image in the size of height 341px and width 241px or leave it as default.")
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    director = models.CharField(default="Undefined", max_length=100)
    protagonist = models.CharField(default="Undefined", max_length=100)

    def __str__(self):
        return self.title

    def short_desc(self):
        if len(self.body) <= 50:
            return self.body
        else:
            return self.body[:50] + '...'
