
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import Application
from .forms import *


class Index(ListView):
    model = 'Model'
    template_name = ''
    context_object_name = 'Books'

    def get_queryset(self):
        pass

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main'
        context['Books'] = Books


class Form(CreateView):
    form_class = Application
    template_name = ''
    success_url = 'home'

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form, 'title': 'Order'}


class Reg(CreateView):
    form_class = RegistrFrom # Django форма для регистрации

    template_name = 'reg.html' # ссылка на шаблон (где хранится это html)
    success_url = reverse_lazy('Entrance') # В случае успешной регистрации пользователя перенаправлет туда

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form, 'title': 'Registr'}

    def post(self, request, *args, **kwargs):
        pass

class Log(LoginView):
    form_class = Entrance
    template_name = ''
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form, 'title': 'Entrance'}





