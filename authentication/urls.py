from django.urls import path
from authentication.views import LogInView, LogOutView, RegisterView

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
