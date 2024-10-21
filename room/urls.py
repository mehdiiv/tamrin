from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render
from room.views import *

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')

urlpatterns = [
    path('', RoomsListView.as_view(), name = 'rooms_list'),
    path('create/', RoomCreateView.as_view(), name = 'room_create'),
    path('<int:room_pk>/', RoomDetailView.as_view(), name = 'room_detail'),
]