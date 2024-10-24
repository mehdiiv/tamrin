from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView , DetailView
from .forms import BuildingForm
from .models import Building
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


class RequiredLoginView(LoginRequiredMixin, TemplateView):
   pass

class BuildingCreateView(RequiredLoginView):
    template_name = 'building/form.html'

    def get(self, request):
        return render(request, self.template_name, { 'form' : BuildingForm })

    def post(self, request):
      form = BuildingForm(request.POST)
      form.instance.creator = request.user
      if form.is_valid():
          object = form.save()
          return redirect('building_detail', object.id)
      return render(request, 'building/form.html', { 'form': form })

class BuildingListView(RequiredLoginView):

    template_name = 'building/list.html'

    def get(self, request):
        context = {
            'objects': Building.objects.filter(creator = request.user )
        }
        return render(request, self.template_name, context)

class BuildingDetailView(UserPassesTestMixin, RequiredLoginView):

    template_name = 'building/detail.html'

    def get(self, request, pk):
        context = { 'building': self.object }

        return render(request, self.template_name, context)

    def test_func(self):
        self.object = get_object_or_404(Building, id = self.kwargs['pk'])
        return self.object.creator_id == self.request.user.id

class BuildingUpdateView(RequiredLoginView):
    template_name = 'building/form.html'

    def get(self, request ,pk):
        object = get_object_or_404(Building, pk = pk)
        context = {
            'form' : BuildingForm(instance = object)
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
       object = get_object_or_404(Building, pk = pk)
       form = BuildingForm(request.POST, instance = object)
       if form.is_valid():
           object = form.save()
           return redirect('building_detail', object.id)
       return render(request, 'building/form.html', { 'form': form })

class BuildingDeleteView(RequiredLoginView):
    def get(self, request, pk):
        building = get_object_or_404(Building, pk = pk)
        building.delete()
        return redirect('building_list')

class SendEmailView(RequiredLoginView):
    def get(self, request):
      subject = 'hello, {0}'.format(self.request.user.username)
      context = {'username': self.request.user.username}
      body = render_to_string('mails/sample.html', context)
      email = EmailMultiAlternatives(subject, "",'', [self.request.user.email])
      email.attach_alternative(body, "text/html")
      email.send()
      return redirect('building_list')
