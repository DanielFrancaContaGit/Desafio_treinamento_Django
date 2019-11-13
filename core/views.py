from django.shortcuts import render
from django.views import generic
from .models import Canais
from .models import Frases
from .models import Habilidades

# Create your views here.

class HomeViews(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['Canais'] = Canais.objects.all()
        context['Frases'] = Frases.objects.all()
        context['Habilidades'] = Habilidades.objects.all()
        return context

   