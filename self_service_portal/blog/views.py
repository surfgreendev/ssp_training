from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views import View
from self_service_portal.blog.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/list_post.html"


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "sub_title", "status", "post_image"]
    template_name = "blog/create_post.html"


"""
class PostListView2(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.published.all()
        return render(request, "blog.list_post_2.html", {"posts": posts})
"""
