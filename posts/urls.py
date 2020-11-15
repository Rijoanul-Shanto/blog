from django.urls import path
from posts.views import PostsView, post_details

urlpatterns = [
    path('', PostsView.as_view(), name="posts"),
    path('<int:post_id>/', post_details)
]
