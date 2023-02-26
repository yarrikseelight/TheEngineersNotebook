from django.shortcuts import render
from .models import Post, Author
from django.views import View
from django.urls import reverse
from .forms import CommentForm
from .models import Comment
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect


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
        comments = post.comments.all().order_by("-id")
        return render(request, "blogapp/postdetail.html", {"post":post, "form":form, "comments":comments,})
    
    def post(self,request, slug):
        post = Post.objects.get(slug=slug)
        form = CommentForm(request.POST) 

        if form.is_valid():
            user = request.user
            comment_contents = form.cleaned_data["comment"]
            comment = Comment(comment=comment_contents, user=user, post=Post.objects.get(slug=slug))
            comment.save()
            form=CommentForm()
            return HttpResponseRedirect(reverse("postdetail", args=[slug]))
        
        comments = post.comments.all().order_by("-id")
        return render(request, "blogapp/postdetail.html", {"post":post, "form":form, "comments":comments,})
    

def about(request):
    me = Author.objects.get(firstname="Jere")
    return render(request, "blogapp/about.html", {"me":me})



