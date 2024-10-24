from django.shortcuts import render
from django.views.generic import TemplateView
from strdisplay.forms import StrdisplayForm

class StrdisplayCreateView(TemplateView):
  template_name = 'strdisplay/form.html'

  def get(self, request):
    context = {'form': StrdisplayForm }
    return render(request, self.template_name, context)

class StrdisplayShowView(TemplateView):
  template_name = 'strdisplay/show.html'
  def post(self ,request):
    form = StrdisplayForm(request.POST)
    if form.is_valid():
      textinput = form.cleaned_data['textinput']
      return render(request, self.template_name)
    return render(request, 'strdisplay/form.html', { 'form' : form })
