from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'self_service_portal.blog'
    verbose_name = 'Blog'
