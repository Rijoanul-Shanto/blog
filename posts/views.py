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
def post_details(request):
    return render(request, 'posts/blog-post.html')
