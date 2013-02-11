from django.views.generic import ListView, DetailView

from .models import Post


class PublishedPostsMixin(object):
    def get_queryset(self):
        return self.model.objects.live()


class PostListView(PublishedPostsMixin, ListView):
    model = Post


class PostDetailView(PublishedPostsMixin, DetailView):
    model = Post
