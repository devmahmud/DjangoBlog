from django.shortcuts import render
from django.views.generic import TemplateView


class PostListView(TemplateView):
    template_name = 'blog/post-list.html'

class PostDetailView(TemplateView):
    template_name = 'blog/post-detail.html'

class PostSearchView(TemplateView):
    template_name = 'blog/post-search.html'
