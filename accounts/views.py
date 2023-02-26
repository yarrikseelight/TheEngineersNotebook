from django.shortcuts import render
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blogapp.models import Post
# Create your views here.

class RegisterView(View):
    def get(self, request):
       form = UserCreationForm()
       return render(request, "accounts/register.html", {"form":form})


    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            posts = Post.objects.order_by('-date')[:3]
            return render(request, "blogapp/frontpage.html", {"posts":posts})

        return render(request, "accounts/register.html", {"form":form,})


def logout_view(request):
    logout(request)
    

