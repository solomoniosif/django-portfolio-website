from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField

from base.models import BasePublishModel
from base.utils import slugify_pre_save


class Post(BasePublishModel):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, db_index=True)
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_on', '-created_on']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


pre_save.connect(slugify_pre_save, sender=Post)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_images")
    image = CloudinaryField("image", resource_type="image", transformation={"quality": "auto:eco"})

    def __str__(self):
        return self.post.title
