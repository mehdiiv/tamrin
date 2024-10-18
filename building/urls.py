from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render
from building.views import *

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')

urlpatterns = [
    path('create/', BuildingCreateView.as_view(), name='building_create'),
    path('', BuildingListView.as_view(), name= 'building_list'),
    path('<int:pk>/', BuildingDetailView.as_view(), name='building_detail'),
    path('<int:pk>/update/', BuildingUpdateView.as_view(), name='building_update'),
    path('<int:pk>/delete/', BuildingDeleteView.as_view(), name='building_delete'),
    path('send_email/', SendEmailView.as_view(), name='send_email'),
]