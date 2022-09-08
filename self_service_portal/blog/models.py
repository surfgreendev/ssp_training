from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.TextField(blank=True, null=True)
    post_image = models.ImageField(upload_to="", blank=True, null=True)
    url_slug = models.SlugField(
        max_length=50, unique=True, help_text="Enter a unique slug name"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


"""
class PostImage(models.Model):
    pass


class PostMeta(models.Model):
    meta_title = models.CharField(_("Meta Title"), max_length=50)
    meta_description = models.TextField(_("Meta Description"))
"""
