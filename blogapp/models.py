from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    intro = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    text = models.TextField()
    date = models.DateField(auto_now=True)
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
