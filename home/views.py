from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignupView(CreateView):
    template_name = 'home/register.html'
    form_class = UserCreationForm
    success_url = '/smart/notes/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('notes:list')
        return super().get(request, *args, **kwargs)

def welcome(request):
    return render(request, 'home/welcome.html')


class HomeView(TemplateView):
    template_name = 'home/welcome.html'




class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
