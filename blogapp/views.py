from django.shortcuts import render
from .models import Post, Author
from django.views import View
from .forms import CommentForm

# Create your views here.


class IndexView(View):
    def get(self, request):
        posts = Post.objects.order_by('-date')[:3]
        return render(request, "blogapp/frontpage.html", {"posts":posts})
    

def posts(request):
    posts = Post.objects.order_by('-date')
    return render(request, "blogapp/posts.html", {"posts":posts})


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post.views += 1
        post.save()
        form = CommentForm()
        return render(request, "blogapp/postdetail.html", {"post":post, "form":form})
    
    def post(self,request, slug):
        post = Post.objects.get(slug=slug)
        form = CommentForm()
        return render(request, "blogapp/postdetail.html", {"post":post, "form":form})
    

def about(request):
    me = Author.objects.get(firstname="Jere")
    return render(request, "blogapp/about.html", {"me":me})
