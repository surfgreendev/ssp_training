from django.contrib import admin
from self_service_portal.blog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "url_slug", "created_on", "updated_on"]
    readonly_fields = ["url_slug"]
