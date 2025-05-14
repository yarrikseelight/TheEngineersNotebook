from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    intro = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    text = models.TextField()
    date = models.DateField(default=timezone.now)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profilepic = models.ImageField(upload_to="images")

    def __str__(self):
        return (f"{self.firstname}  {self.lastname}")
    

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return (f"{self.post} - - - - - - - - {self.comment}")
    