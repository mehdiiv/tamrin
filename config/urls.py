from django.urls import path, include
from django.views.generic import TemplateView
from django.shortcuts import render
from account.views import *

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')

urlpatterns = [
    path('' , HomeView.as_view(), name='home'),
    path('building/', include('building.urls')),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password-reset', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset/done', ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('strdisplay/', include('strdisplay.urls')),

]
