from django.urls import path
from posts.views import PostsView, PostDetailsView

urlpatterns = [
    path('', PostsView.as_view(), name="posts"),
    path('<int:post_id>/', PostDetailsView.as_view(), name="post_details"),
]
