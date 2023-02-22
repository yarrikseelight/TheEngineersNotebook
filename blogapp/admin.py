from django.contrib import admin
from .models import Post, Author
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]
    list_filter = ["date"]
    readonly_fields=("slug",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname"]





admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)