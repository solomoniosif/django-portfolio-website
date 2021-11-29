from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    inlines = [PostImageAdmin, ]
    summernote_fields = ('text',)

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
