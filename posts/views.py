from django.shortcuts import render
from django.views import View
import requests


# POSTS VIEW ENDPOINT
class PostsView(View):
    @staticmethod
    def get(request):
        page = request.GET.get('page', 20)
        response = requests.get('https://jsonplaceholder.typicode.com/posts?_page={}&_limit=5'.format(page))
        data = response.json()

        return render(request, 'blog-listing.html', {"data": data})


# POST DETAILS VIEW ENDPOINT
class PostDetailsView(View):
    @staticmethod
    def get(request, post_id):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/{}'.format(post_id))
        post = response.json()

        response = requests.get('https://jsonplaceholder.typicode.com/posts/{}/comments'.format(post_id))
        comments = response.json()

        return render(request, 'blog-post.html', {"post": post, "comments": comments})
