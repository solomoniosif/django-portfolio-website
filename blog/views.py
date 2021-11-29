from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from hitcount.views import HitCountDetailView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView, SuccessMessageMixin

from blog.forms import PostForm, PostImageForm
from blog.models import Post, PostImage


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(status='PU')


class PostDetailView(HitCountDetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'
    count_hit = True

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get(self.slug_url_kwarg)
        post = get_object_or_404(Post, slug=slug)
        if self.request.user.is_staff:
            return post
        if post.status == 'PR':
            messages.error(self.request, "This post is private")
            return Post.objects.none()
        elif post.status == 'DR':
            messages.warning(self.request, "This post is not yet published")
            return Post.objects.none()
        else:
            return post


class PostImageInlineFormset(InlineFormSetFactory):
    model = PostImage
    form_class = PostImageForm
    fields = '__all__'
    extra_forms = 1
    can_delete = True

    def get_factory_kwargs(self):
        factory_kwargs = super().get_factory_kwargs()
        factory_kwargs.update({'extra': self.extra_forms})
        return factory_kwargs


class PostCreateWithInlinesView(LoginRequiredMixin, CreateWithInlinesView):
    model = Post
    form_class = PostForm
    inlines = [PostImageInlineFormset, ]
    template_name = 'blog/post_create.html'
    success_url = None

    # def forms_valid(self, form, inlines):
    #     # form.instance.publi = self.request.user
    #     self.object = form.save()
    #     response = self.form_valid(form)
    #     for formset in inlines:
    #         for form in formset:
    #             new_photo = form.save(commit=False)
    #             new_photo.post = self.object
    #             new_photo.save()
    #     messages.success(self.request, f"<b>{self.object.title}</b> created successfully")
    #     return response

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.slug})


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     template_name = 'blog/post_create.html'
#     form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    permission_required = 'post.delete_post'
