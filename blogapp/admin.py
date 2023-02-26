from django.contrib import admin
from .models import Post, Author, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]
    list_filter = ["date"]
    readonly_fields=("slug",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname"]

class CommentAdmin(admin.ModelAdmin):
    list_filter = ["post", "user", "date",]





admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)