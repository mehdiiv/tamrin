from django.shortcuts import render, redirect ,get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from room.forms import RoomForm
from building.models import Building
from room.models import Room
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class RequiredLoginView(LoginRequiredMixin, TemplateView):
   pass

class RoomsListView(RequiredLoginView):
    template_name = 'room/list.html'

    def get(self, request, pk):
        context = {
            'objects': Room.objects.filter(building_id = pk )
        }
        return render(request, self.template_name, context)

class RoomCreateView(RequiredLoginView):
    template_name = 'room/form.html'

    def get(self, request, pk ):
        return render(request, self.template_name, { 'form' : RoomForm })

    def post(self, request, pk):
        form = RoomForm(request.POST)
        form.instance.building_id = pk
        if form.is_valid():
            object = form.save()
            return redirect('room_detail', pk, object.id)
        return render(request, 'room/form.html', { 'form': form })

class RoomDetailView(UserPassesTestMixin,RequiredLoginView):
    template_name = 'room/detail.html'

    def get(self, request, pk, room_pk):

        context = { 'room': self.object }
        return render(request, self.template_name, context)

    def test_func(self):
        self.object = get_object_or_404(Room, id = self.kwargs['room_pk'])
        return self.object.building_id == self.kwargs['pk']



class RoomUpdateView(RequiredLoginView):
    template_name = 'room/form.html'

    def get(self, request , pk, room_pk ):
        object = get_object_or_404(Room, pk = room_pk)
        context = {
            'form' : RoomForm(instance = object)
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, room_pk):
       object = get_object_or_404(Room, pk = room_pk)
       form = RoomForm(request.POST, instance= object)
       if form.is_valid():
           object = form.save()
           return redirect('room_detail', pk, object.id)
       return render(request, 'room/form.html', { 'form': form })

class RoomDeleteView(RequiredLoginView):
    def get(self, request, pk, room_pk):
        object = get_object_or_404(Room, pk = room_pk)
        object.delete()
        return redirect('rooms_list', pk)
