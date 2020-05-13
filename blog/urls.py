from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostSearchView
)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('detail/', PostDetailView.as_view(), name='post_detail'),
    path('search/', PostSearchView.as_view(), name='post_search'),
]
