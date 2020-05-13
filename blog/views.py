from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin
from taggit.models import Tag

from .models import Post


class PostListView(ListView):
    paginate_by = 3
    template_name = 'blog/post-list.html'

    def get_queryset(self):
        queryset =  Post.published.all()
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=[tag])
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs.get('tag_slug')
        return context


class PostDetailView(FormMixin, DetailView):
    template_name = 'blog/post-detail.html'

    def get_object(self):
        obj = get_object_or_404(Post, status='published',
            slug=self.kwargs.get('slug'),
            publish__year=self.kwargs.get('year'),
            publish__month=self.kwargs.get('month'),
            publish__day=self.kwargs.get('day')
        )
        return obj


class PostSearchView(TemplateView):
    template_name = 'blog/post-search.html'
