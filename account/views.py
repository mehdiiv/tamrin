from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserLogin
from django.contrib.auth import login, authenticate, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views as auth_views


class LoginView(TemplateView):
    template_name = 'account/login.html'
    def get(self, request):
        context = {
            'loginform': UserLogin
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
      form = UserLogin(request.POST)
      if form.is_valid():
         username= form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(request, username = username, password = password)
         if user != None:
            login(request, user)
            return redirect('home')
         else:
            form.add_error('username', 'invlid username or password')
            return render(request, self.template_name, { 'loginform' : form })


class LogoutView(TemplateView):
   def get(self, request):
      logout(request)
      return redirect('login')

class ResetPasswordView(SuccessMessageMixin, auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'

class ResetPasswordDoneView(auth_views.PasswordResetDoneView):
   template_name = 'registration/password_reset_done.html'