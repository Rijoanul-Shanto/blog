from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin


# LOGIN VIEW ENDPOINT

class LogInView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = 'Login Successful!'
    redirect_authenticated_user = True


# LOGOUT VIEW ENDPOINT
class LogOutView(LogoutView):
    success_message = 'Logout Successful!'
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.ERROR, 'Successfully logged out.')
        return response
