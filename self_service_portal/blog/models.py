from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from self_service_portal.blog.managers import PostManager


# Create your models here.
class Post(models.Model):
    class PostStatus(models.TextChoices):
        DRAFT = "DRAFT", _("Entwurf")
        PUBLISHED = "PUBLISHED", _("Veroeffentlicht")

    status = models.CharField(
        _("Blog Status"),
        max_length=20,
        choices=PostStatus.choices,
        default=PostStatus.DRAFT,
    )
    title = models.CharField(max_length=50)
    sub_title = models.TextField(blank=True, null=True)
    post_image = models.ImageField(upload_to="", blank=True, null=True)
    url_slug = models.SlugField(
        max_length=50, unique=True, help_text="Enter a unique slug name"
    )
    published_on = models.DateTimeField(
        _("Vereoffentlich am"),
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
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

        if self.status == self.PostStatus.PUBLISHED:
            self.published_on = timezone.now()
        super(Post, self).save(*args, **kwargs)

    objects = PostManager()


"""
class PostImage(models.Model):
    pass

class PostMeta(models.Model):
    meta_title = models.CharField(_("Meta Title"), max_length=50)
    meta_description = models.TextField(_("Meta Description"))

class PostCategory(models.Model):
    pass

class PostTag(models.Model):
    pass

class PostComment(models.Model):
    pass
"""
