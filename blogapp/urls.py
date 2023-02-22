from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path("", views.IndexView.as_view(), name="frontpage"),
    path("posts", views.posts, name="posts"),
    path("about", views.about, name="about"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="postdetail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)