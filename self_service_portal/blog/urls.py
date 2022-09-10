from django.urls import path

from self_service_portal.blog.views import PostCreateView, PostListView

app_name = "users"
urlpatterns = [
    path("posts/", view=PostListView.as_view(), name="post-list"),
    path("posts/create/", view=PostCreateView.as_view(), name="post-create"),
]
