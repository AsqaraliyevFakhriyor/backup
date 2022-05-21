from ..models import Post

from taggit.models import Tag

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

# Post app views.

""" Get list of all aricles """
class PostListView(ListView):
    # model = Post
    object_list = Post.published.all()
    context_object_name = "post"
    paginate_by = 4
    template_name = 'post/post_list.html'

    def get_tags(self, tag_slug = None, *args, **kwargs):
        if tag_slug:
            tag = get_object_or_404(
                Tag,
                tag_slug=tag_slug
            )
            object_list = object_list.filter(tags__in=[tag])
            .0

    


"""GET specific Post with Post id """
class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = 'post'


""" POST (edit) specific Post with Post id """
class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'summary', 'body', 'photo', 'status')
    template_name = "post/post_edit.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


""" POST (delete) specific aritcle with Post id """
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy('post:post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


""" POST (create) Post """
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView,):
    model = Post
    fields = ('title', 'summary', 'body', 'photo',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    template_name = "post/post_create.html"