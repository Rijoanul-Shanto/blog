from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from authentication.forms import CustomUserCreationForm


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
        # Check that user signup is allowed
        if not self.request.user.is_authenticated:
            return redirect('/')
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.ERROR, 'Successfully logged out.')
        return response


# Register VIEW ENDPOINT
class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = '/'
    form_class = CustomUserCreationForm
    success_message = 'Registration Successful!'

    def dispatch(self, request, *args, **kwargs):
        # Check that user signup is allowed
        if self.request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
