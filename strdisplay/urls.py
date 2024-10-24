from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render
from strdisplay.views import *

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')

urlpatterns = [
    path('create/', StrdisplayCreateView.as_view(), name = 'strdisplay_create'),
    path('create/display', StrdisplayShowView.as_view(), name = 'show_strdisplay' )
]
