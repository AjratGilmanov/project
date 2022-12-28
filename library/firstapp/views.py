
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


class Index(ListView):
    model = 'Model'
    template_name = ''
    context_object_name = ''


    def get_queryset(self):
        pass
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main'

